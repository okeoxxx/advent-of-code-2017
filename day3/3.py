import math
from pprint import pprint as pp
input = 312051

a = math.sqrt(input)
layers = math.ceil(a)

field = 0

for i in range(1,layers+2,2):
    layer_area = i*i - field
    if field + layer_area >= input:
        for j in range(4):
            changer = False
            for k in range(layer_area//4):
                if field + j*layer_area//4 + k == input:
                    res = layers//2 + abs(k-layers//2)
                    print('Solution 1st part:',res)
                    changer = True
                    break
            if changer:
                break

    else:
        field += layer_area

#solution of second part

layers = [1]

while max(layers) < input:
    layers.append(layers[-1]+len(layers)*8)

d = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def f(board):
    suma = 0
    for dir in d:
            n = board[y + dir[0]][x + dir[1]]
            if n:
                    suma += n
    board[y][x] = suma
    if suma>input:
        print('Solution 2nd part:',suma)
    return((board,suma<input))

size = 16
board = [[[] for i in range(size)] for j in range(size)]

x = size//2
y = size//2
board[y][x] = 1

changer = True
num = 1
while changer:
    x += 1
    y += 1
    for i in range(num*8):
        if i // (2*num) == 0:
            y -= 1
        elif i // (2*num) == 1:
            x -= 1
        elif i // (2*num) == 2:
            y += 1
        else:
            x += 1
        board,changer = f(board)
        if not changer:
            break
    num += 1
