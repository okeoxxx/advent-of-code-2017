check = 12683008
state = 'A'

states = {
            'A':{
                0:{'v':1,'m':1,'s':'B'},
                1:{'v':0,'m':-1,'s':'B'}
                },
            'B':{
                0:{'v':1,'m':-1,'s':'C'},
                1:{'v':0,'m':1,'s':'E'}
                },
            'C':{
                0:{'v':1,'m':1,'s':'E'},
                1:{'v':0,'m':-1,'s':'D'}
                },
            'D':{
                0:{'v':1,'m':-1,'s':'A'},
                1:{'v':1,'m':-1,'s':'A'}
                },
            'E':{
                0:{'v':0,'m':1,'s':'A'},
                1:{'v':0,'m':1,'s':'F'}
                },
            'F':{
                0:{'v':1,'m':1,'s':'E'},
                1:{'v':1,'m':1,'s':'A'}
                },

        }

tape = [0]
cur = 0

for n in range(check):
    if cur < 0:
        cur += 1
        tape.insert(0,0)
    elif cur == len(tape):
        tape.append(0)
    action = states[state][tape[cur]]
    tape[cur] = action['v']
    cur += action['m']
    state = action['s']
    if n % 1000000 == 0:
        print(n)

print('Solution 1st part:', sum(tape))
