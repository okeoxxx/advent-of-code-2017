from collections import deque

file = open('10.txt','r')
file = file.readline()[:-1]

lengths = [int(num) for num in file.split(',')]

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

result1 = circulate(lengths,1)
print('Solution 1st part:', result1[0] * result1[1])

#second part
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

print('Solution 2nd part:', hash)
