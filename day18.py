f = open('input/day18.txt')
lines = [line.rstrip() for line in f.readlines()]

import re
ints = lambda x: [int(i) for i in re.findall('-?\d+', x)]

faces = lambda x, y, z: {(x + 1, y, z), (x - 1, y, z), \
                         (x, y + 1, z), (x, y - 1, z), \
                         (x, y, z + 1), (x, y, z - 1)}

cubes, visited = set(), set()
bound = max(max(ints(l)) for l in lines) + 1
for line in lines: cubes.add(tuple(ints(line)))

flood = [(-1, -1, -1)]
while flood:
    x = flood.pop()
    flood += [f for f in (faces(*x) - cubes - visited) \
        if all(-1 <= c <= bound for c in f)]
    visited |= {x}

part1 = sum((f not in cubes) for c in cubes for f in faces(*c))
part2 = sum((f in visited) for c in cubes for f in faces(*c))

print(f'part 1: {part1}')
print(f'part 2: {part2}')
