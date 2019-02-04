file = open('2.txt','r')

rows = []

while True:
    row = file.readline()[:-1]
    if row == '':
        break
    rows.append([int(i) for i in row.split('\t')])

counter = 0
for r in rows:
    counter += max(r)-min(r)

print('Solution 1st part:',counter)

counter = 0
for r in rows:
    changer = False
    for i,num in enumerate(r):
        for index in range(i):
            if num % r[index] == 0:
                changer = True
                counter += num // r[index]
                break
            elif r[index] % num == 0:
                changer = True
                counter += r[index] // num
                break
        if changer:
            break

print('Solution 2nd part:',counter)
