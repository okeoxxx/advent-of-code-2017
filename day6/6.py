file = open('6.txt','r')

bank = file.readline()[:-1]
bank = [int(num) for num in bank.split('\t')]

results = []
counter = 0
while bank not in results:
    results.append(bank.copy())
    max_block = max(bank)
    chosen_block_index = bank.index(max_block)
    bank[chosen_block_index] = 0
    for i in range(1,max_block+1):
        if chosen_block_index+i == len(bank):
            chosen_block_index -= len(bank)
        bank[chosen_block_index+i] += 1
    counter += 1

print('Solution 1st part:',counter)
print('Solution 2nd part:',counter-results.index(bank))
