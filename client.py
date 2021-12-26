import socket
import threading
import time
import sys
import random

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8080))
msg = "client 999: hi"
print(msg)
client.send(msg.encode())
time.sleep(5)
client.send(msg.encode())
client.send(msg.encode())
client.close()

#sys.exit(0)

def work(name):
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
  client.close()


ts = list()
clients = 10

for i in range(clients):
  name = f"thread-{i}"
  t =  threading.Thread(target=work, args=(name,), name=name, daemon=True)
  ts.append(t)
  t.start()

for t in ts:
  t.join()
