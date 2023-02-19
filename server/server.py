import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

body = [
    b'Hellow World!',
]

length = b'Content-Length: ' + str(len(b'\n'.join(body))).encode()

header = [
    b'HTTP1.1 200 OK',
    length,
    b'Connection: close',
    b'Content-type: text/html'
]

response = [
    *header,
    b'',
    *body,
    b'\n',
]

serversocket.bind(('localhost', 8000))
serversocket.listen(1)

(clientsocket, address) = serversocket.accept()

msg = clientsocket.recv(4096)
r = b'\n'.join(response)
print(r)
clientsocket.send(r)

clientsocket.close()
