import socket
import time
import signal
import sys
import threading

#signal.signal(signal.SIGINT, signal.SIG_DFL)

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = ("127.0.0.1", 8080)
serv.bind(ip)
print(f"Server started {ip}")

serv.listen(1)

(c, addr) = serv.accept()
msg = c.recv(1024)
print(msg.decode())
print("Closing server client in 5")
time.sleep(2)
print("Closing client socket")
c.close()
print("Closing server socket in 5")
time.sleep(5)
print("Closing server socket")
serv.close()

sys.exit(1)

def server():
    while True:
        print("waiting for client connection")
        (c, sock) = serv.accept()
        print("client connected")
        try:
            while True:
                data = c.recv(1024)
                if not data:
                    print("socket closed - client sent empty data")
                    break
                print((len(data), data.decode()))
        except socket.error:
            print("Socket error occured")
        except KeyboardInterrupt:
            break
        finally:
            print("Server closing client")
            c.close()

    print("server socket closing")
    serv.close()

t = threading.Thread(target=server, name="serverThread", daemon=True)
t.start()
print("should print")
t.join()

print("at end")
