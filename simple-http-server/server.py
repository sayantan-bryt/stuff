import argparse
import os
import socket
import typing as t


COUNTER = 0


def parse_headers(request: str) -> dict:
  headers = {}
  print('Request str:', request)
  print(f'Line separator: {os.linesep=}')
  request = request.replace('\r', '')
  request_data = request.split('\n')
  request_path =  request_data[0]
  print('Request:', request_path)
  http_meth, http_file_path, http_protocol = request_path.split(' ')
  print(
    'http method:', http_meth,
    '\nHttp File Path:', http_file_path,
    '\nHttp Protocol:', http_protocol,
  )
  request_headers = request_data[1:]
  for line in request_headers:
    separator_pos = line.find(':')
    header_type, header_info = line[:separator_pos], line[separator_pos+1:]
    headers[header_type.lower()] = header_info

  print(f"Request Headers: {headers}")
  return headers


def get_response(headers: dict) -> str:
  global COUNTER
  print(f"Response Headers: {headers}")
  COUNTER += 1
  return f"Connection Succeeded: {COUNTER}"


def handle_connection(client: socket.socket):
  got = client.recv(1024)
  data = got.decode()
  headers = parse_headers(data)
  resp = get_response(headers)
  response = f'HTTP/1.1 200 OK\n\n{resp}'
  client.send(response.encode())
  client.close()


def server(address: t.Tuple):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  sock.bind(address)
  sock.listen(5)
  while True:
    client, addr = sock.accept()
    print("Connection: ", addr)
    no_data = handle_connection(client)
    if no_data:
      break

  sock.close()


def main(args_list: t.Sequence[str] | None = None):
  parser = argparse.ArgumentParser()
  parser.add_argument('--host', default='127.0.0.1')
  parser.add_argument('--port', type=int, default='5000')
  parser.add_argument('--run', action='store_true')
  args = parser.parse_args(args=args_list)

  host, port = args.host, args.port
  server((host, port))
  return 0


if __name__ == '__main__':
  raise SystemExit(main())
