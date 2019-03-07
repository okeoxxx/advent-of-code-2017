import copy

file = open('22.txt','r')

board = []

row = 0
extend = 200
while True:
    line = file.readline()[:-1]
    if line == '':
        break
    board.append(['.']*extend+[i for i in line]+['.']*extend)
    row += 1

a = len(board[0])
for i in range(extend):
    board.insert(0, ['.']*a)
    board.append(['.']*a)

marks = 'v>^<v>^<'
dirs = {'^': (0,-1),'>': (1,0),'v': (0,1),'<': (-1,0)}

def move(mark,pos,b):
    if b[pos[1]][pos[0]] == '#':
        b[pos[1]][pos[0]] = '.'
        return (marks[marks.find(mark)-1],0)
    else:
        b[pos[1]][pos[0]] = '#'
        return (marks[marks.find(mark)+1],1)

def part1(b):
    x = len(board[0])//2
    y = len(board)//2
    mark = '^'
    pos = (x,y)
    counter = 0
    for burst in range(10000):
        mark,c = move(mark,pos,b)
        x += dirs[mark][0]
        y += dirs[mark][1]
        pos = (x,y)
        counter += c
    return counter

print('Solution 1st part:', part1(copy.deepcopy(board)))

def changer(mark,pos,b):
    global counter
    if b[pos[1]][pos[0]] == '#':
        b[pos[1]][pos[0]] = 'F'
        return marks[marks.find(mark)-1]
    elif b[pos[1]][pos[0]] == 'W':
        b[pos[1]][pos[0]] = '#'
        counter += 1
        return mark
    elif b[pos[1]][pos[0]] == 'F':
        b[pos[1]][pos[0]] = '.'
        return marks[marks.find(mark)+2]
    else:
        b[pos[1]][pos[0]] = 'W'
        return marks[marks.find(mark)+1]

x = len(board[0])//2
y = len(board)//2
mark = '^'
pos = (x,y)
counter = 0

for burst in range(10000000):
    mark = changer(mark,pos,board)
    x += dirs[mark][0]
    y += dirs[mark][1]
    pos = (x,y)

print('Solution 2nd part:', counter)
