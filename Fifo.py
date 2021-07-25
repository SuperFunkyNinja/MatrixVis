import os

if os.path.exists("myfifo"):
  os.remove("myfifo")
else:
  print("The file does not exist")

FIFO = 'myfifo'

os.mkfifo(FIFO)

value = []
intValue = []

for i in range(32):
    value.append(0)
    intValue.append(0)

def fifoRead():

    with open(FIFO) as fifo:
        value = fifo.readline()
        
##        if '<' not in value:
        
        value = value.split(';') 
        for i in range(32):
            intValue[i] = int(value[i])
          
    print(intValue)

while True:
    fifoRead()
    print('test')


with open(FIFO) as fifo:
    print(fifo)
    for line in fifo:
      ## print(line)
      value = line.split(';')
      for i in range(32):
          intValue[i] = int(value[i])
          
      
      print(intValue)