import os
import time
from collections import Counter
import math
import hashlib
from pynput import mouse, keyboard
import threading
from queue import Queue
import logging

# Configurer le logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Variable globale pour capturer les événements utilisateur
user_input = b""
event_queue = Queue()  # File d'attente pour les événements utilisateurs

# Calcul de l'entropie de Shannon
def shannon_entropy(data: bytes) -> float:
    if not data:
        return 0
    counts = Counter(data)
    total_len = len(data)
    entropy = -sum((count / total_len) * math.log2(count / total_len) for count in counts.values())
    return entropy

# Mélange d'événements utilisateur avec os.urandom pour générer plus d'entropie
def mix_entropy_with_user_input(entropy: bytes, user_input: bytes) -> bytes:
    user_event_entropy = str(time.time()).encode('utf-8') + user_input
    mixed_entropy = hashlib.blake2b(entropy + user_event_entropy, digest_size=32).digest()  # Blake2 pour un meilleur mélange
    return mixed_entropy

# Fonction de capture des événements utilisateur via souris et clavier
def capture_user_events(stop_event):
    def on_move(x, y):
        log_message = f"Mouse moved to ({x}, {y}) at {time.time()}"
        logger.debug(log_message)
        event_queue.put(log_message.encode('utf-8'))
    
    def on_click(x, y, button, pressed):
        log_message = f"Mouse clicked at ({x}, {y}) with {button} at {time.time()}"
        logger.debug(log_message)
        event_queue.put(log_message.encode('utf-8'))
    
    def on_scroll(x, y, dx, dy):
        log_message = f"Mouse scrolled at ({x}, {y}) at {time.time()}"
        logger.debug(log_message)
        event_queue.put(log_message.encode('utf-8'))
    
    def on_press(key):
        try:
            log_message = f"Key {key.char} pressed at {time.time()}"
            logger.debug(log_message)
            event_queue.put(log_message.encode('utf-8'))
        except AttributeError:
            log_message = f"Special key {key} pressed at {time.time()}"
            logger.debug(log_message)
            event_queue.put(log_message.encode('utf-8'))
    
    def on_release(key):
        if key == keyboard.Key.esc:
            stop_event.set()
            return False
    
    # Écoute des événements souris et clavier dans des threads séparés
    mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
    keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    
    # Démarrer les threads
    mouse_listener.start()
    keyboard_listener.start()
    
    # Attendre que le stop_event soit déclenché
    stop_event.wait()
    
    # Arrêter les listeners
    mouse_listener.stop()
    keyboard_listener.stop()

# Fonction qui traite les événements collectés dans une file d'attente
def process_user_input():
    global user_input
    while not event_queue.empty():
        user_input += event_queue.get()

# Test de l'entropie
def test_entropy(byte_size: int, samples: int):
    global user_input  # Accès à la variable globale
    entropy_sum = 0
    start_time = time.time()

    # Créer un événement pour arrêter la capture
    stop_event = threading.Event()

    # Lancer la capture d'événements utilisateur dans un thread
    capture_thread = threading.Thread(target=capture_user_events, args=(stop_event,))
    capture_thread.start()

    # Attendre un peu pour accumuler des événements utilisateurs
    time.sleep(1)  # Attendre que l'utilisateur fasse quelques actions

    # Traitement des événements collectés
    process_user_input()

    # Test de l'entropie pendant un échantillon
    for _ in range(samples):
        random_bytes = os.urandom(byte_size)
        mixed_entropy = mix_entropy_with_user_input(random_bytes, user_input)
        entropy = shannon_entropy(mixed_entropy)
        entropy_sum += entropy
        logger.debug(f"Entropy for sample: {entropy:.2f} bits")

    # Arrêter la capture d'événements
    stop_event.set()

    # Attendre que le thread se termine
    capture_thread.join()

    elapsed_time = time.time() - start_time
    avg_entropy = entropy_sum / samples
    max_entropy = 8 * byte_size

    # Log des résultats
    logger.info(f"Taille des clés: {byte_size} octets")
    logger.info(f"Nombre d'échantillons: {samples}")
    logger.info(f"Entropie moyenne observée: {avg_entropy * byte_size:.2f} bits")
    logger.info(f"Entropie théorique maximale: {max_entropy} bits")
    logger.info(f"Temps écoulé: {elapsed_time:.4f} sec")
    logger.info("-")

# Test avec une clé de 32 octets (256 bits)
test_entropy(32 , 100000)  # Augmenter le nombre d'échantillons pour plus d'entropie
