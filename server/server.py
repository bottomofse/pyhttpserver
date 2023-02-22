import socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def separate_headerbody(request):
    msg_list = request.split(b'\r\n')
    for m in msg_list:
        print(m.decode('utf-8'))

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

while True:
    (clientsocket, address) = serversocket.accept()
    msg = clientsocket.recv(4096)
    separate_headerbody(msg)
    r = b'\n'.join(response)
    clientsocket.send(r)
    clientsocket.close()
