import re
file = open('12.txt','r')

rows = {}

while True:
    line = file.readline()[:-1]
    if line == '':
        break
    nums = re.findall(r'\d+', line)
    rows[int(nums.pop(0))]=[int(num) for num in nums]

all_nums = set(rows)
groups = []

def make_connection(rest_nums):
    group = set()
    a = len(group)
    group.add(rest_nums.pop())
    while a < len(group):
        a = len(group)
        connected = set()
        for num in group:
            for connection in rows[num]:
                connected.add(connection)
        group = group.union(connected)
    return group

while all_nums:
    new_group = make_connection(all_nums)
    groups.append(new_group)
    all_nums = all_nums.difference(new_group)

print('Solution 1st part:', len(groups[0]))
print('Solution 2nd part:', len(groups))
