file = open('20.txt','r')

particles = {}
distances = []
particle = 0

while True:
    line = file.readline()
    if line == '':
        break
    particles[particle] = {'p':[],'v':[],'a':[]}

    for j in line.split():
        x,y,z = list(map(int,j[j.find('<')+1:j.find('>')].split(',')))
        particles[particle][j[0]] = [x,y,z]
    pos = particles[particle]['p']
    distances.append(sum(abs(k) for k in pos))
    particle += 1

winners = []
collided = []

for time in range(500):
    min_dist = min(distances)
    winners.append((distances.index(min_dist),min_dist))
    positions = []
    for p in particles:
        for axes in range(3):
            particles[p]['v'][axes] += particles[p]['a'][axes]
            particles[p]['p'][axes] += particles[p]['v'][axes]
        pos = particles[p]['p']
        distances[p] = sum(abs(k) for k in pos)
        if p not in collided:
            if pos in positions:
                collided.append(p)
                for x in range(p):
                    if particles[x]['p'] == pos and x not in collided:
                        collided.append(x)
                        break
            else:
                positions.append(pos)

print('Solution 1st part:', winners[-1][0])
print('Solution 2nd part:', len(particles)-len(collided))
