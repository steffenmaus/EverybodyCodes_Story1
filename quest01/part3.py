import re

with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]
    intlines = [[int(n) for n in re.findall(r'-?\d+', line)] for line in lines]


def eni(n, exp, mod):
    total = 0
    score = 1
    loop = 0
    scores = set()
    scores_ordered = []
    while loop < exp:
        score *= n
        score %= mod
        skipped = False
        if score in scores:
            scores_ordered = scores_ordered[scores_ordered.index(score):]
            size = len(scores_ordered)
            skips = (exp - loop) // size
            skipped = skips > 0
            loop += skips * size
            total += skips * sum(scores_ordered)
            score = scores_ordered[-1]
            scores = set()
            scores_ordered = []
        if not skipped:
            scores.add(score)
            scores_ordered.append(score)
            total += score
            loop += 1
    return total


results = set()
for l in intlines:
    a, b, c, x, y, z, m = l
    results.add(eni(a, x, m) + eni(b, y, m) + eni(c, z, m))

print(max(results))
