#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import socket
import threading

class ServerSocket:
    def __init__(self, mode='localhost', port=None):
        self.mode = mode
        if mode == "localhost":
            self.host = mode
        elif mode == "public":
            self.host = socket.gethostname()
        else:
            self.host = mode

        self.port = port
        if type(self.port) != int:
            print("port must be an int")
            raise ValueError

        # 创建基于TCP的流式socket通信
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self._socket.setblocking(0) # TODO: socket Errno 35 in OSX
        self._socket.bind((self.host, self.port))

    def run(self):
        self._socket.listen(5)
        print 'Server start at: %s:%s' %(self.host, self.port)

        def tcplink(sock, addr):
            print 'Accept new connection from %s:%s...' % addr
            sock.send('')
            while True:
                data = sock.recv(1024)
                time.sleep(1)
                if data == 'exit' or not data:
                    break
                print data
            sock.close()
            print 'Connection from %s:%s closed' % addr

        while True:
            sock, addr = self._socket.accept()
            print sock
            t = threading.Thread(target=tcplink, args=(sock, addr))
            t.start()