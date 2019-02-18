def generator(value, factor, M=1):
        while True:
            value = value * factor % 2147483647
            if value % M == 0:
                yield value & 0xffff

A, B = 679, 771#65, 8921
gA, gB = generator(A, 16807), generator(B, 48271)
print('Solution 1st part:', sum(next(gA) == next(gB) for i in range(40000000)))
gA, gB = generator(A, 16807, 4), generator(B, 48271, 8)
print('Solution 2nd part:', sum(next(gA) == next(gB) for i in range(5000000)))
