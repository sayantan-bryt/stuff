#!/d/Programs/Python/Python37/python
from threading import Thread
import concurrent.futures
import requests
from requests import Session
from requests.adapters import HTTPAdapter
import time
import sys

URL = input('Enter URL:\n')
# max_retries = 5
# req_adapter = HTTPAdapter(max_retries=max_retries)
# session = Session()

def request_endpoint(thread_num):
    global URL
    print(URL)
    # try:
        # r = requests.get(URL, timeout=30)
        # # session.mount(URL, req_adapter)
        # print("Connection %s: %s" % (thread_num, r.status_code))
    # except BaseException as e:
        # print('connection error:' + str(e))


if __name__ == '__main__':
    num_req = eval(input('Enter number of concurrent requests you want to make:\n'))

    t1 = time.perf_counter()
    # thread_list = list()
    # for i in range(num_req):
    #     x = Thread(target=request_endpoint, args=(i+1,), daemon=True)
    #     thread_list.append(x)
    #     x.start()

    try:
        # for i, thread in enumerate(thread_list):
        #     thread.join()
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_req) as concurrent_connections:
            concurrent_connections.map(request_endpoint, range(num_req))
    except KeyboardInterrupt:
        sys.exit(1)
    finally:
        t2 = time.perf_counter()
        print('Time required: %.3f seconds' % (t2-t1))
