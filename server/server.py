import socket
from .request.request import Request

class BaseServer:
    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        """
        仮のレスポンス用
        """
        body = [
            b'Hello World!',
        ]
        length = b'Content-Length: ' + str(len(b'\n'.join(body))).encode()
        header = [
            b'HTTP1.1 200 OK',
            length,
            b'Connection: close',
            b'Content-type: text/html'
        ]
        self.response = [
            *header,
            b'',
            *body,
            b'',
        ]

    def get_response_bytes(self):
        return b'\r\n'.join(self.response)

    def start_listen(self):
        self.socket.bind((self.ip, self.port))
        self.socket.listen(1)

        while True:
            (clientsocket, address) = self.socket.accept()
            msg = clientsocket.recv(4096)
            request = Request(msg)
            clientsocket.send(self.get_response_bytes())
            clientsocket.close()

def separate_headerbody(request):
    msg_list = request.split(b'\r\n')
    for m in msg_list:
        print(m.decode('utf-8'))
