from collections import deque
from pprint import pprint as pp

input = 'wenycdww'

def circulate(lengths,repeat):
    lst = list(range(256))
    circle = deque(lst)
    move = 0
    for skip_size,num in enumerate(repeat*lengths):
        sublist = []
        for i in range(num):
            sublist.append(circle.popleft())
        circle.extendleft(sublist)
        m = num+skip_size
        move += m
        circle.rotate(-m)

    circle.rotate(move%len(lst))
    return list(circle)

def knot_hash(file):
    lengths = [ord(ch) for ch in file] + [17,31,73,47,23]

    sparse_hash = circulate(lengths,64)

    def dense(sp_hash):
        dense = []
        for i in range(16):
            new_lst = sp_hash[i*16:(i+1)*16]
            a = 0
            for j in range(16):
                a ^= new_lst[j]
            dense.append(a)
        return dense

    dense_hash = dense(sparse_hash)

    hash = ''
    for num in dense_hash:
        if 'x' not in hex(num)[-2:]:
            hash += hex(num)[-2:]
        else:
            hash += '0'+ hex(num)[-1]

    return hash

counter = 0
table = []

for row in range(128):
    table.append([])
    hash = knot_hash('{}-{}'.format(input,row))
    bin_hash = bin(int(hash, 16))[2:].zfill(128)
    counter += bin_hash.count('1')
    for square in bin_hash:
        if square == '1':
            table[row].append('#')
        else:
            table[row].append('.')

print('Solution 1st part:', counter)

dirs = [(0,-1),(0,1),(1,0),(-1,0)]

def make_group(num,x,y):
    table[y][x] = str(num)
    for dir in dirs:
        new_x = x+dir[0]
        new_y = y+dir[1]

        if new_x < 0 or new_y < 0:
            continue
        try:
            if table[new_y][new_x] == '#':
                make_group(num,new_x,new_y)
        except:
            continue

num = 0
for y in range(128):
    for x in range(128):
        if table[y][x] == '#':
            num += 1
            make_group(num,x,y)

print('Solution 2nd part:', num)
