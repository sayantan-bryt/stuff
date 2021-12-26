import socket
import time
import signal
import sys

signal.signal(signal.SIGINT, signal.SIG_DFL)

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = ("127.0.0.1", 8080)
serv.bind(ip)
print(f"Server started {ip}")

serv.listen(10)

(c, sock) = serv.accept()
msg = c.recv(4096)
print(msg.decode())
c.close()
serv.close()

sys.exit(1)

while True:
  (c, sock) = serv.accept()
  print("client connected")
  while True:
    data = c.recv(1024)
    if not data:
      break
    print(data.decode())
  print("Server closing client")
  c.close()

serv.close()

