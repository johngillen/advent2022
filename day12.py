f = open('input/day12.txt')
lines = [line.rstrip() for line in f.readlines()]

grid = [[ord(c)-ord('a') for c in row] for row in lines]
for x, row in enumerate(grid):
  for y, point in enumerate(row):
    if point == -14: start = (x, y); grid[x][y] = 0
    if point == -28: end = (x, y); grid[x][y] = 25
lx, ly = len(grid), len(grid[0])

neighbors = lambda x, y: [(x, y + 1), (x + 1, y), (x - 1, y), (x, y - 1)]

def traverse(todo, done):
    next = []
    for x, y in todo:
        for dx, dy in neighbors(x, y):
            if not (0 <= dx < lx and 0 <= dy < ly): continue
            if grid[dx][dy] > grid[x][y] + 1: continue
            if (dx, dy) in done: continue
            if (dx, dy) == end: return True, ()
            next.append((dx, dy))
            done.add((dx, dy))
    return False, next

def path(start):
    todo, done = [start], set([start])
    for i in range(1000):
        ended, todo = traverse(todo, done)
        if ended: return i + 1
    return 1000

part1 = path(start)
part2 = min([path((x, y)) for x in range(lx) for y in range(ly) if grid[x][y] == 0])

print(f'part 1: {part1}')
print(f'part 2: {part2}')
