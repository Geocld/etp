#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from etp.application import Stp

stp = Stp()

stp.run(port=9090)