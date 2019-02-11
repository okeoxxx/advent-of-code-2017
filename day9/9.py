file = open('9.txt','r')

file = file.readline()[:-1]
garbage = False
counter1 = 0
counter2 = 0
score = 0
i = 0

while i < len(file):
    ch = file[i]
    if not garbage:
        if ch == '{':
            score += 1
        elif ch == '}':
            counter1 += score
            score -= 1
    else:
        if ch not in '!>':
            counter2 += 1
    if ch == '<':
         garbage = True
    elif ch == '>':
         garbage = False
    elif ch == '!':
        i += 1
    i += 1

print('Solution 1st part:',counter1)
print('Solution 2nd part:',counter2)
