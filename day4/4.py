file = open('4.txt','r')

part1 = 0
part2 = 0
while True:
    line = file.readline()[:-1]
    if line == '':
        break
    line = line.split(' ')
    if len(line) == len(set(line)):
        part1 +=1
        a = []
        for word in line:
            a.append(set(word))
        a = set(frozenset(i) for i in a)
        if len(line) == len(set(a)):
            part2 += 1

print('Solution 1st part:',part1)
print('Solution 2nd part:',part2)
