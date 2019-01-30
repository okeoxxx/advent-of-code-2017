file = open('1.txt','r')
captcha = file.readline()
lst = [int(num) for num in captcha[:-1]]

counter = 0
for i,num in enumerate(lst):
    if num == lst[i-1]:
        counter += num

print('Solution 1st part:',counter)

counter = 0
for i,num in enumerate(lst):
    if num == lst[i-len(lst)//2]:
        counter += num

print('Solution 2nd part:',counter)
