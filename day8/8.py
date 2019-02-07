file = open('8.txt','r')

vars_str = []
cmds = []

while True:
    line = file.readline()[:-1]
    if line == '':
        break
    line = line.split(' ')
    exec('{}=0'.format(line[0]))
    vars_str.extend([line[0],line[4]])
    exec('{}=0'.format(line[4]))
    line[1] = '+=' if line[1] == 'inc' else '-='
    condition = ' '.join(line) + ' else 0'
    exec('cmds.append("'+condition+'")')

result2 = 0

for i in range(len(cmds)):
    exec(cmds[i])
    vars = []
    for v in vars_str:
        exec('vars.append({})'.format(v))
    result1 = max(vars)
    result2 = result1 if result1 > result2 else result2

print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
