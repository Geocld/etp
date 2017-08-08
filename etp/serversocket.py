#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

class ServerSocket:
    def __init__(self, mode='localhost', port=8080):
        self.mode = mode
        self.port = port
        if mode == "localhost":
            self.host = mode
        elif mode == "public":
            self.host = socket.gethostname()
        else:
            self.host = mode

        # 创建基于TCP的流式socket通信,非阻塞
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setblocking(0)
        self._socket.bind((self.host, self.port))

    def run(self):
        self._socket.listen(5)
        print 'Waiting for connection...'