import socket

class ClientSocket:
    def __init__(self, mode='localhost', port=8080, recv_bytes=2048, single_use=True):
        self.mode = mode
        self.port = port
        if mode == "localhost":
            self.host = mode
        elif mode == "public":
            self.host = socket.gethostname()
        else:
            self.host = mode

        self.recv_bytes = recv_bytes
        self.single_use = single_use

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, data):
        self._socket.connect((self.host, self.port))
        self._socket.send(data)

    def close(self):
        pass