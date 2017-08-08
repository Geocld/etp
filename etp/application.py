#!/usr/bin/env python
# -*- coding: utf-8 -*-

from etp.serversocket import ServerSocket
from etp.clientsocket import ClientSocket

class Stp:
    def __init__(self, socket_type='server'):
        self.socket_type = socket_type

    def run(self):
        ss = ServerSocket()
        ss.run()

    def send(self, data):
        cs = ClientSocket()
        cs.send(data)
