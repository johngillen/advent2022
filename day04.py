f = open('input/day04.txt')
lines = [line.rstrip() for line in f.readlines()]

import re

pairs = 0
allpairs = 0

for line in lines:
    a, b, c, d = [int(n) for n in re.findall(r'\d+', line)]

    elf1 = set(range(a, b + 1))
    elf2 = set(range(c, d + 1))

    if elf1 | elf2 in (elf1, elf2):
        pairs += 1
    if elf1 & elf2:
        allpairs += 1

part1 = pairs
part2 = allpairs

print(f'part 1: {part1}')
print(f'part 2: {part2}') 
