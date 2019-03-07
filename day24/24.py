file = open('24.txt','r')

components = []

while True:
    line = file.readline()[:-1]
    if line == '':
        break
    line = line.split('/')
    components.append([int(num) for num in line])

bridges = []

def connect(pin,used_com):
    for i,c in enumerate(components):
        if pin in c and i not in used_com:
            connect(c[c.index(pin)-1],used_com+[i])
    bridges.append(used_com)

connect(0,[])

strengths = []
for b in bridges:
    count = 0
    for c in b:
        count += sum(components[c])
    strengths.append((len(b), count))

print('Solution 1st part:', max(s[1] for s in strengths))
print('Solution 2nd part:', max(strengths)[1])
