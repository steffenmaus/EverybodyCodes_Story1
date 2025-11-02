import re

with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]
    intlines = [[int(n) for n in re.findall(r'-?\d+', line)] for line in lines]


def eni(n, exp, mod):
    lor = []
    score = pow(n, exp-5, mod)

    for _ in range(5):
        score *= n
        score %= mod
        lor.append(score)
    return int("".join([str(x) for x in reversed(lor[-5:])]))


results = set()

for l in intlines:
    a,b,c,x,y,z,m = l
    results.add(eni(a,x,m) + eni(b,y,m) + eni(c,z,m))

print(max(results))