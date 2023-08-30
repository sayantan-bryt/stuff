import socket

# https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html


def create(address: tuple[str, int]) -> None:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind(address)
    server.listen(5)
    while True:
        sock, _ = server.accept()
        handle_client(sock)


def handle_client(client: socket.socket) -> None:
    while True:
        data = client.recv(1024)  # keep sending data to client.
        if not data:
            break
        strdata = str(data)
        print(f"Client sent: {strdata=}")
        payload = ("Server recieved: %s" % (strdata + '\n')).encode('ascii')
        client.send(payload)


create(('127.0.0.1', 5555))
