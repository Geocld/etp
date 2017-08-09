#!/usr/bin/env python
# -*- coding: utf-8 -*-

from etp.serversocket import ServerSocket
from etp.clientsocket import ClientSocket

class Stp:
    def __init__(self, socket_type='server'):
        self.socket_type = socket_type

    def run(self, mode = '', port=8080):
        ss = ServerSocket(port = port)
        ss.run()

    def send(self, data, mode='localhost', port=8080, recv_bytes=2048, single_use=True):
        cs = ClientSocket(mode = mode, port = port, recv_bytes = recv_bytes, single_use = single_use)
        cs.send(data)
