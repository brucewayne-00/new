import threading
import time
import random

buffer = []
BUFFER_SIZE = 5
TOTAL_ITEMS = 10

# Synchronization primitives
mutex = threading.Lock()
empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)

def producer():
    for _ in range(TOTAL_ITEMS):
        item = random.randint(1, 100)
        empty.acquire()
        with mutex:
            buffer.append(item)
            print(f"[Producer] Produced: {item}")
        full.release()
        time.sleep(random.uniform(0.1, 0.3))

def consumer():
    for _ in range(TOTAL_ITEMS):
        full.acquire()
        with mutex:
            item = buffer.pop(0)
            print(f"[Consumer] Consumed: {item}")
        empty.release()
        time.sleep(random.uniform(0.1, 0.3))

# Start producer and consumer threads 
t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()

t1.join()
t2.join()

print("Producer and Consumer have finished.")
