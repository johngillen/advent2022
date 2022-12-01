f = open('input/day01.txt')
lines = [line.rstrip() for line in f.readlines()]

elves = []

calories = 0
for line in lines:
    try:
        calories += int(line)
    except:
        elves += [calories]
        calories = 0

part1 = max(elves)
part2 = sum(sorted(elves)[-3:])

print(f'part 1: {part1}')
print(f'part 2: {part2}')
