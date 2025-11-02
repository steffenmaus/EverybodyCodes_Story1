import re

with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]
    intlines = [[int(n) for n in re.findall(r'-?\d+', line)] for line in lines]

snakes = set()
for l in intlines:
    x, y = l
    snakes.add((x, y))

for _ in range(100):
    next = set()
    for s in snakes:
        x, y = s
        if y == 1:
            next.add((1, x))
        else:
            next.add((x + 1, y - 1))
    snakes = next

total = 0
for s in snakes:
    total += s[0] + (100 * s[1])
print(total)
