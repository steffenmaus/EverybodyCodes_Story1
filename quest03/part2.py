import re

with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]
    intlines = [[int(n) for n in re.findall(r'-?\d+', line)] for line in lines]

snakes = set()
for l in intlines:
    x, y = l
    snakes.add((x, y))

i = 0
while not all([x[1] == 1 for x in snakes]):
    next = set()
    for s in snakes:
        x, y = s
        if y == 1:
            next.add((1, x))
        else:
            next.add((x + 1, y - 1))
    snakes = next
    i += 1
print(i)
