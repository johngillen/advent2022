f = open('input/day07.txt')
lines = [line.rstrip() for line in f.readlines()]

pwd = []
directories = {'/': 0}

for line in lines:
    if '$ cd' in line:
        if '..' not in line:
            pwd.append(line.split()[-1])
        else:
            pwd.pop()
    elif line.split()[0].isdigit():
        size = int(line.split()[0])
        key = '/'
        for dir in pwd:
            key += (dir + '/') if dir != '/' else ''
            if key not in directories:
                directories[key] = 0
            directories[key] += size

part1 = sum([v for v in directories.values() if v <= 100000])
part2 = min([v for v in directories.values() if v >= \
    (30000000 - (70000000 - directories['/']))])

print(f'part 1: {part1}')
print(f'part 2: {part2}')
