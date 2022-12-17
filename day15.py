f = open('input/day15.txt')
lines = [line.rstrip() for line in f.readlines()]

import re
ints = lambda x: [int(i) for i in re.findall('-?\d+', x)]

dists = {}
row = 2000000

for line in lines:
    sx, sy, bx, by = ints(line)
    dists[(sx, sy)] = abs(sx - bx) + abs(sy - by)

lo, hi = float('inf'), float('-inf')
for (x, y), d in dists.items():
    dy = abs(row - y)
    if dy > d: continue
    dx = d - dy
    lo, hi = min(lo, x - dx), max(hi, x + dx)
part1 = hi - lo

def tune(freq):
    todo = []
    for (x, y), d in dists.items():
        dy = abs(freq - y)
        if dy > d: continue
        dx = d - dy
        todo.append((x - dx, x + dx))
    todo.sort(); prev = todo.pop(0)[1]
    for a, b in todo:
        if a > prev: return prev + 1; break
        prev = max(b, prev)
    return False

for i in range(4000000):
    if x:= tune(i):
        part2 = x * 4000000 + i; break

print(f'part 1: {part1}')
print(f'part 2: {part2}')
