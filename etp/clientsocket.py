#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

class ClientSocket:
    def __init__(self, mode='localhost', port=None, recv_bytes=2048, single_use=True):
        self.mode = mode
        self.port = port
        if type(self.port) != int:
            print("port must be an int")
            raise ValueError

        if mode == "localhost":
            self.host = mode
        elif mode == "public":
            self.host = socket.gethostname()
        else:
            self.host = mode

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.recv_bytes = recv_bytes

        self.single_use = single_use
        if not self.single_use:
            self.closed = False
        self.used = False

    def send(self, data):
        if self.single_use:
            if self.used:
                print "You cannot use a single-use socket twice"
                raise RuntimeError
            self._socket.connect((self.host, self.port))
            self.closed = False

        # 将data endoce
        if type(data) != str:
            data = bytes(data, 'utf-8')

        data = data.decode('utf-8').encode('utf-8')

        self._socket.send(data)
        self.used = True

    def close(self):
        if not self.closed:
            self._socket.close()
            self.closed = True