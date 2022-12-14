f = open('input/day14.txt')
lines = [line.rstrip() for line in f.readlines()]

import re
ints = lambda x: [int(i) for i in re.findall(r'-?\d+', x)]

grid = [['.' for _ in range(1000)] for _ in range(1000)]
floor = 0

for line in lines:
    coords = ints(line)
    cx, cy = coords[:2]
    for dx, dy in zip(*[iter(coords[2:])]*2):
        rx = 1 if cx <= dx else -1
        ry = 1 if cy <= dy else -1
        for dx in range(cx, dx + rx, rx):
            for dy in range(cy, dy + ry, ry):
                grid[dx][dy] = '#'
        floor = max(floor, dy)
        cx, cy = dx, dy
floor += 2

def fall(grid):
    cx, cy = 500, 0
    try:
        while True:
            if grid[cx][cy + 1] == '.': cy += 1; continue
            if grid[cx - 1][cy + 1] == '.': cx -= 1; cy += 1; continue
            if grid[cx + 1][cy + 1] == '.': cx += 1; cy += 1; continue
            grid[cx][cy] = 'o'
            return (cx, cy) != (500, 0)
    except:
        return False

abyss = [row.copy() for row in grid]

part1, result = 0, fall(abyss)
while result: part1 += 1; result = fall(abyss)

for i in range(len(grid)): grid[i][floor] = '#'
part2, result = 1, fall(grid)
while result: part2 += 1; result = fall(grid)

print(f'part 1: {part1}')
print(f'part 2: {part2}')
