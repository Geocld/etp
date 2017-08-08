#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

from etp.application import Stp


stp = Stp(socket_type='client')

while True:
    cmd = raw_input("Please input msg:")
    stp.send(cmd, port=9090)