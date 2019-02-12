import re
from time import time
start = time()
file = open('13.txt','r')

layers = {}

while True:
    line = file.readline()[:-1]
    if line == '':
        break
    nums = re.findall(r'\d+', line)
    layers[int(nums[0])]=int(nums[1])

def get_caught(delay):
    caught = []
    for ps in range(99):
        if ps in layers:
            cycle = (layers[ps]-1)*2
            if caught and delay:
                return caught
            elif (ps+delay) % cycle == 0:
                caught.append(ps)
    return caught

severity = 0
for c in get_caught(0):
    severity += c * layers[c]

print('Solution 1st part:', severity)

for delay in range(0,10000000,2): #step 2 just because layer 2 has range 2 => avoid being caught in layer 1
    if delay % 4 == 0 or delay % 6 == 0: #avoid being caught in layers 0 and 6
        continue
    if not get_caught(delay):
        print('Solution 2nd part:', delay)
        break

print('Completed in', time() - start, 'seconds.')
