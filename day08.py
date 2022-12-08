f = open('input/day08.txt')
lines = [line.rstrip() for line in f.readlines()]

part1 = 0
part2 = 0

grid = [[int(c) for c in line] for line in lines]
scenic = [[1 for _ in line] for line in lines]

for x in range(len(grid)):
    for y, tree in enumerate(grid[x]):
        up = [grid[n][y] for n in range(0, x)][::-1]
        down = [grid[n][y] for n in range(x + 1, len(grid))]
        left = [grid[x][n] for n in range(0, y)][::-1]
        right = [grid[x][n] for n in range(y + 1, len(grid[0]))]

        for axis in [up, down, left, right]:
            for t in axis:
                if tree <= t:
                    break
            else:
                part1 += 1
                break

        for axis in [up, down, left, right]:
            if axis == []:
                scenic[x][y] *= 0
            else:
                scene = [n for n in axis if n >= tree]
                scene = axis.index(scene[0]) + 1 if scene != [] else len(axis) 
                scenic[x][y] *= scene

part2 = max([max(row) for row in scenic])

print(f'part 1: {part1}')
print(f'part 2: {part2}')
