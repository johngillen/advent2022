f = open('input/day04.txt')
lines = [line.rstrip() for line in f.readlines()]

import re

pairs = 0
allpairs = 0

for line in lines:
    a, b, c, d = [int(n) for n in re.findall(r'\d+', line)]

    elf1 = set(range(int(a), int(b) + 1))
    elf2 = set(range(int(c), int(d) + 1))

    if elf1.issubset(elf2) or \
       elf2.issubset(elf1):
        pairs += 1
    if elf1.intersection(elf2):
        allpairs += 1

part1 = pairs
part2 = allpairs

print(f'part 1: {part1}')
print(f'part 2: {part2}') 
