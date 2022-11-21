#!/usr/bin/python3

from datetime import datetime, timezone, timedelta
from sys import argv

year, day = datetime.now(timezone(timedelta(hours=-5))).year, \
            datetime.now(timezone(timedelta(hours=-5))).day

if len(argv) == 2:
    day = int(argv[1])
if len(argv) == 3:
    year, day = int(argv[1]), int(argv[2])

program = open(f'day{day:0>2}.py', 'w')

program.write(f'''f = open('input/day{day:0>2}.txt')
lines = [line.rstrip() for line in f.readlines()]

for line in lines:
    print(line)

part1 = 0
part2 = 0

print(f'part 1: {{part1}}')
print(f'part 2: {{part2}}')
''')

# print(f'day{day:0>2}.py')
