f = open('input/day04.txt')
lines = [line.rstrip() for line in f.readlines()]

import re

part1 = 0
part2 = 0

for line in lines:
    a, b, c, d = [int(n) for n in re.findall(r'\d+', line)]

    elf1 = set(range(a, b + 1))
    elf2 = set(range(c, d + 1))

    if elf1 | elf2 in (elf1, elf2):
        part1 += 1
    if elf1 & elf2:
        part2 += 1

print(f'part 1: {part1}')
print(f'part 2: {part2}') 
