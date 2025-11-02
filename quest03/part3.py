import re

with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]
    intlines = [[int(n) for n in re.findall(r'-?\d+', line)] for line in lines]

snakes = set()
for l in intlines:
    x, y = l
    snakes.add((x - 1, y - 1))

done = set()
i = 0
while snakes:
    stepsize = 1
    for d in done:
        stepsize *= d
    next = set()
    for s in snakes:
        x, y = s
        cycle = x + y + 1
        n_x = (x + stepsize) % cycle
        n_y = (y - stepsize) % cycle
        if n_y != 0:
            next.add((n_x, n_y))
        else:
            done.add(cycle)
    snakes = next
    i += stepsize
print(i)
