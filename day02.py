f = open('input/day02.txt')
lines = [line.rstrip() for line in f.readlines()]

strat1 = 0
strat2 = 0

for line in lines:
    elf, me = line.split(' ')
    elf = {'A': 0, 'B': 1, 'C': 2}[elf]
    me = {'X': 0, 'Y': 1, 'Z': 2}[me]

    strat1 += me       + (me - elf + 1) % 3 * 3 + 1
    strat2 += (me * 3) + (me + elf - 1) % 3     + 1


part1 = strat1
part2 = strat2

print(f'part 1: {part1}')
print(f'part 2: {part2}')
