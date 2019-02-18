file = open('19.txt','r')

board = []

while True:
    line = file.readline()[:-1]
    if line == '':
        break
    board.append([])
    for i in line:
        board[-1].append(i)

def intersection(x,y):
    for d,v in dirs.items():
        new_x = x + v[0]
        new_y = y + v[1]
        if board[new_y][new_x] != ' ' and (new_x,new_y) not in path:
            return d

dirs = {'^': (0,-1),'>': (1,0),'v': (0,1),'<': (-1,0)}

x,y = board[0].index('|'), 0
path = []
d = 'v'
text = ''

while board[y][x] != ' ':
    path.append((x,y))
    new_field = board[y][x]
    if new_field == '+':
        d = intersection(x,y)
    elif new_field.isalpha():
        text += new_field
    x = x + dirs[d][0]
    y = y + dirs[d][1]

print('Solution 1st part:', text)
print('Solution 2nd part:', len(path))
