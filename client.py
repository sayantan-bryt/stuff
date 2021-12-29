import socket
import threading
import time
import sys
import random

if 1:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 8080))
    msg = "client 999: hi"
    print(msg)
    client.send(msg.encode())
    #print("Sending ''")
    #time.sleep(2)
    #client.send(b"")
    time.sleep(5)
    #print(msg)
    client.send(msg.encode())
    time.sleep(5)
    print(msg)
    client.send(msg.encode())
    time.sleep(5)
    print(msg)
    client.send(msg.encode())
    time.sleep(5)
    #client.send(b'')
    #client.send(b'')
    #client.send(b'')
    print("waiting for 5 secs after empty string")
    time.sleep(5)
    print("should be closed by now")
    time.sleep(5)
    client.close()

sys.exit(1)

def work(name):
    client = None
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("127.0.0.1", 8080))
        msg = f"{name} : hi"
        print(msg)
        time.sleep(2)
        client.send(msg.encode())
        if random.random() <= 0.7:
            print("70% chance")
            time.sleep(2)
            more = msg + " More DATA"
            client.send(more.encode())
        print(f"{name} Closing")
    except BrokenPipeError as BB:
        #print(f"{name} : Broken Pipe:  {BB}")
        while True:
            try:
                print(f"{name}: reconnecting")
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect(("127.0.0.1", 8080))
                msg = "Resending: " + msg
                print(msg)
                client.send(msg.encode())
                break
            except BrokenPipeError:
                print(f"{name}: Retrying...")
                continue
            except Exception as e:
                print(f"{name}: Exception occured" + str(e))
                break
    except Exception as e:
        print(f"{name}: exception caused {str(e)}")
    finally:
        if client:
            client.close()


ts = list()
clients = 10

for i in range(clients):
    name = f"thread-{i}"
    t = threading.Thread(target=work, args=(name,), name=name, daemon=True)
    ts.append(t)
    t.start()

for t in ts:
    t.join()
