import m
import time
import logging

log = logging.getLogger("MainServer")
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)


# main_server
def main():
    while True:
        time.sleep(.5)
        log.info(f"[Main Server] {m.num_threads=}")

    m.imp_fn("ssam")


if __name__ == "__main__":
    raise SystemExit(main())
