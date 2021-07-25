import re
import time
import argparse
import random
import math
import os

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message

SENS = 8

if os.path.exists("myfifo"):
  os.remove("myfifo")
else:
  print("The file does not exist")

FIFO = 'myfifo'
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

while True:    
    with open(FIFO) as fifo:
        value = fifo.readline()        
        value = value.split(';') 
        for i in range(32):
            try:
                intValue[i] = int(value[i])# / SENS
            except: print('exception')
        print(value)
            
#     average = sum(intValue)/len(intValue)
#     
#     if average < 3: SENS -= 0.1
#     if average > 3: SENS += 0.1
#     if SENS > 8: SENS = 8
#     if SENS < 1: SENS = 1
    
    
#        if average > 2:
 #           SENS = SENS + 0.5
  #      if average < 2:
   #         SENS = SENS - 0.5
    
##    print(intValue)
    #print(average,SENS)
    write(intValue)