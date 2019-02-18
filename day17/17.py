from collections import deque

input = 301

circle = deque([])

for i in range(2018):
    circle.rotate(-input)
    circle.append(i)


print('Solution 1st part:', circle[0])

for i in range(2018,50000001):
    circle.rotate(-input)
    circle.append(i)

print('Solution 2nd part:', circle[circle.index(0)+1])
