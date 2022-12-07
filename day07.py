f = open('input/day07.txt')
lines = [line.rstrip() for line in f.readlines()]

part1 = 0
part2 = 0

path = []
directories = {'/': 0}

for line in lines:
    if '$ cd' in line:
        if line.split()[-1] == '..':
            path.pop()
        else:
            path.append(line.split()[-1])
    elif line.split()[0].isdigit():
        size = int(line.split()[0])
        pathname = '/'
        for dir in path:
            pathname += (dir + '/') if dir != '/' else ''
            if pathname not in directories:
                directories[pathname] = 0
            directories[pathname] += size

part1 += sum([v for v in directories.values() if v <= 100000])
part2 = min([v for v in directories.values() if v >= \
    (30000000 - (70000000 - directories['/']))])

print(f'part 1: {part1}')
print(f'part 2: {part2}')
