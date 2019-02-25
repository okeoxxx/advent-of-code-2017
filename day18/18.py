file = open('18.txt','r')

vars0 = {}
vars1 = {}
cmds = []

while True:
    line = file.readline()[:-1].split()
    if not line:
        break
    if line[1].isalpha():
        vars0[line[1]] = 0
        vars1[line[1]] = 1
    cmds.append(line)

queue = {0:[],1:[]}

def play(vars,row,ind,task=0):
    played = {}
    while True:
        cmd = cmds[row]
        f,x,y = cmd[0],cmd[1],cmd[-1]
        val_x = vars[x] if x.isalpha() else int(x)
        val_y = vars[y] if y.isalpha() else int(y)
        if f == 'snd':
            if task == 1:
                played[x] = val_x
            else:
                global counter
                if ind == 1:
                    counter += 1
                queue[(ind+1)%2].append(val_x)
        elif f == 'set':
            vars[x] = val_y
        elif f == 'add':
            vars[x] += val_y
        elif f == 'mul':
            vars[x] *= val_y
        elif f == 'mod':
            vars[x] %= val_y
        elif f == 'rcv':
            if task == 1:
                if x in played:
                    if played[x]:
                        print('Solution 1st part:', played[x])
                        break
            else:
                if queue[ind]:
                    vars[x] = queue[ind].pop(0)
                else:
                    return row
        elif f == 'jgz':
            if val_x > 0:
                row += val_y
                continue
        row += 1

play(vars0.copy(),0,0,1)
row0 = 0
row1 = 0

result = True
counter = 0
while result != counter:
    result = counter
    row0 = play(vars0,row0,0)
    row1 = play(vars1,row1,1)

print('Solution 2nd part:', counter)
