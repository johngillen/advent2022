f = open('input/day02.txt')
lines = [line.rstrip() for line in f.readlines()]

score = {'R': 1, 'P': 2, 'S': 3}

rps = ['R', 'P', 'S']

win = {'R': 'P', 'P': 'S', 'S': 'R'}
lose = {'R': 'S', 'P': 'R', 'S': 'P'}
tie = {'R': 'R', 'P': 'P', 'S': 'S'}

strat1, strat2 = 0, 0

for line in lines:
    elf, me = line.split(' ')
    elf = {'A': 'R', 'B': 'P', 'C': 'S'}[elf]
    me = {'X': 'R', 'Y': 'P', 'Z': 'S'}[me]

    strat1 += score[me]
    if me == win[elf]:
        strat1 += 6
    elif me == tie[elf]:
        strat1 += 3
    
    if me == 'R':
        me = lose[elf]
    elif me == 'P':
        me = elf
        strat2 += 3
    elif me == 'S':
        me = win[elf]
        strat2 += 6
    strat2 += score[me]

part1 = strat1
part2 = strat2

print(f'part 1: {part1}')
print(f'part 2: {part2}')
