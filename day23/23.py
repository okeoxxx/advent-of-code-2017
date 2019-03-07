file = open('23.txt','r')

cmds = []
vars = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0}

while True:
    line = file.readline()[:-1]
    if line == '':
        break
    cmds.append(line.split())

counter = 0
row = 0
while True:
    try:
        cmd = cmds[row]
    except IndexError:
        break
    X = vars[cmd[1]] if cmd[1].isalpha() else int(cmd[1])
    Y = vars[cmd[2]] if cmd[2].isalpha() else int(cmd[2])
    if cmd[0] == 'set':
        vars[cmd[1]] = Y
    elif cmd[0] == 'sub':
        vars[cmd[1]] -= Y
    elif cmd[0] == 'mul':
        vars[cmd[1]] *= Y
        counter += 1
    else:
        if X != 0:
            row += Y
            continue
    row += 1

print('Solution 1st part:', counter)

h = 0
for x in range(105700,122700 + 1,17):
    for i in range(2,x//2):
        if x % i == 0:
            h += 1
            break

print('Solution 2nd part:', h)
