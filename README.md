# etp
A minimal and easy TCP server for you.

### Installation

1. Clone the repository : `git clone https://github.com/Geocld/etp.git`
2. Install the package: `python setup.py install`

### Usage

server:(run the server and listen client send data)

```python
from etp.application import Stp

stp = Stp()

stp.run()
```

client:(send data to server)

```python
from etp.application import Stp

stp = Stp(socket_type='client')

while True:
    cmd = raw_input("Please input msg:")
    stp.send(cmd)
```

Very very simple,is it?

### Example

Examples can be found in the `/examples` folder.