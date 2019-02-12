file = open('11.txt','r')
file = file.readline()[:-1]
path = [d for d in file.split(',')]

dirs = {'n':(0,-2),'ne':(1,-1),'se':(1,1),'s':(0,2),'sw':(-1,1),'nw':(-1,-1)}

x,y = 0,0
max_dist = 0

for p in path:
    x += dirs[p][0]
    y += dirs[p][1]
    dx = abs(x)
    dy = (abs(y)-dx)//2
    dist = dx + dy
    if dist > max_dist:
        max_dist = dist

print('Solution 1st part:', dist)
print('Solution 2nd part:', max_dist)
