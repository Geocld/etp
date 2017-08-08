import sys
sys.path.append('../')

from etp.application import Stp


stp = Stp(socket_type='client')

stp.send('client')