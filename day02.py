f = open('input/day02.txt')
lines = [line.rstrip() for line in f.readlines()]

part1 = 0
part2 = 0

for line in lines:
    elf, me = line.split(' ')
    elf = ord(elf) - ord('A')
    me = ord(me) - ord('X')

    part1 += me       + (me - elf + 1) % 3 * 3 + 1
    part2 += (me * 3) + (me + elf - 1) % 3     + 1

print(f'part 1: {part1}')
print(f'part 2: {part2}')
