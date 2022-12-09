f = open('input/day09.txt')
lines = [line.rstrip() for line in f.readlines()]

part1 = [[0 for _ in range(1000)] for _ in range(1000)]
part2 = [[0 for _ in range(1000)] for _ in range(1000)]

rope = [[500, 500] for _ in range(10)]

for line in lines:
    dir, dist = line[0], int(line[1:])
    dir = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}[dir]
    for _ in range(dist):
        rope[0] = list(map(sum, zip(rope[0], dir)))
        for i in range(1, len(rope)):
            for a, b in [(0, 1), (1, 0)]:
                if abs(rope[i - 1][a] - rope[i][a]) > 1:
                    rope[i][a] += 1 if rope[i - 1][a] > rope[i][a] else -1
                    rope[i][b] += 1 if rope[i - 1][b] > rope[i][b] else 0
                    rope[i][b] -= 1 if rope[i - 1][b] < rope[i][b] else 0
            
        part1[rope[1][0]][rope[1][1]] = 1
        part2[rope[-1][0]][rope[-1][1]] = 1

part1 = sum([sum(row) for row in part1])
part2 = sum([sum(row) for row in part2])

print(f'part 1: {part1}')
print(f'part 2: {part2}')
