file = open('7.txt','r')

branch = set()
root = set()

weights = {}
connections = {}

while True:
    row = file.readline()[:-1]
    if row == '':
        break
    words = row.split(' ')
    weights[words[0]] = int(words[1].strip('()'))
    if '->' in words:
        root.add(words[0])
        connections[words[0]] = []
        for w in words[3:]:
            branch.add(w.strip(','))
            connections[words[0]].append(w.strip(','))

result = list(root - branch)[0]
print('Solution 1st part:', result)

def weight(name):
    if name not in connections:
        return weights[name]
    else:
        br = 0
        nums = []
        for n in connections[name]:
            w = weight(n)
            nums.append(w)
            br += w
        if len(set(nums)) > 1:
            for num in set(nums):
                if nums.count(num) == 1:
                    i = nums.index(num)
                    wrong_num = nums[i]
                    right_num = nums[i-1]
                    wrong_name = connections[name][i]
                    print('Solution 2nd part:',weights[wrong_name] - wrong_num + right_num)
                    quit()
        return weights[name] + br

weight(result)
