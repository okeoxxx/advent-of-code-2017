import re
file = open('16.txt','r')

line = [chr(i) for i in range(97,97+16)]
dance = file.read()[:-1].split(',')
results = [''.join(line)]

def spin(move,line):
    move = int(move)
    return line[-move:] + line[:-move]

def exchange(nums,line):
    move = [int(num) for num in re.findall(r'\d+', nums)]
    line[move[0]],line[move[1]] = line[move[1]],line[move[0]]
    return line

def partner(chars,line):
    move = [line.index(ch) for ch in chars if ch.isalpha()]
    line[move[0]],line[move[1]] = line[move[1]],line[move[0]]
    return line

dance_moves = {'s':spin,'x':exchange,'p':partner}

def generator(line):
    while True:
        for d in dance:
            line = dance_moves[d[0]](d[1:],line)
        yield line

DANCE = generator(line)

r = ''.join(next(DANCE))
while r not in results:
    results.append(r)
    r = ''.join(next(DANCE))

last_index = 1000000000 % len(results)

print('Solution 1st part:', results[1])
print('Solution 2nd part:', results[last_index])
