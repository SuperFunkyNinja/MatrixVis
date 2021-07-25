# import re
# import time
# import argparse
# import random
# import math
import os
import subprocess
import sys

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message

SENS = 8
FIFO = '/home/pi/MatrixVis/myfifo'

if os.path.exists(FIFO):
    os.remove(FIFO)
else:
    print("The file does not exist")

os.mkfifo(FIFO)

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=90)

value = []
intValue = []

for i in range(32):
    value.append(0)
    intValue.append(0)
    
def write(value):
    with canvas(device) as draw:
        for i in range(32):
            y = value[i]            
            for j in range(64):
                draw.point((i, y-j), fill="white")            
        return

p = subprocess.Popen('exec ' + '/home/pi/cava/cava', shell = True)

try:
    while True:    
        with open(FIFO, 'r') as f:
            value = f.readline()
            value = value.split(';') 
            for i in range(32):
                try:
                    intValue[i] = int(value[i])# / SENS
                except: pass          
        write(intValue)
        print(intValue)
except KeyboardInterrupt:
    p.kill()
    sys.exit()
    pass