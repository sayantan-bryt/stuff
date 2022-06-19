import threading
import time
import datetime
import logging


log = logging.getLogger("GlobalThread")
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)

num_threads = 0

global_lock = threading.Lock()

def fn():
    """
    Thread that runs for ever
    """
    global num_threads
    with global_lock:
        num_threads += 1
    log.info(f"{num_threads=}")
    while True:
        time.sleep(1)
        with global_lock:
            with open("f.txt", 'w') as f:
                f.write(f"{datetime.datetime.now()}")
        log.info("Updated token")

THREAD_NAME="my_thread"

is_running = False

for i in range(10):
    t = threading.Thread(target=fn, name=THREAD_NAME, daemon=True)
    for th in threading.enumerate():
        is_running = is_running or th.name==THREAD_NAME

    if not is_running:
        t.start()

def imp_fn(name: str) -> str:
    return f"Greetings {name}"
