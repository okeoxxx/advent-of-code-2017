file = open('5.txt','r')

maze = []

while True:
    row = file.readline()[:-1]
    if row == '':
        break
    maze.append(int(row))

m = maze.copy() # copy for second part

counter = 0
i = 0
while True:
    try:
        change = 1
        maze[i] += change
        i += maze[i]-change
        counter += 1
    except IndexError:
        print('Solution 1st part:',counter)
        break

counter = 0
i = 0
while True:
    try:
        change = 1 if m[i] < 3 else -1
        m[i] += change
        i += m[i]-change
        counter += 1
    except IndexError:
        print('Solution 2nd part:',counter)
        break
