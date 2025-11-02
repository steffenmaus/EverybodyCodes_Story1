import re

with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]
    intlines = [[int(n) for n in re.findall(r'-?\d+', line)] for line in lines]


def eni(n, exp, mod):
    lor = []
    score = 1
    for _ in range(exp):
        score *= n
        score %= mod
        lor.append(score)
    return int("".join([str(x) for x in reversed(lor)]))


results = set()

for l in intlines:
    a, b, c, x, y, z, m = l
    results.add(eni(a, x, m) + eni(b, y, m) + eni(c, z, m))

print(max(results))
