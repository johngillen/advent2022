f = open('input/day03.txt')
lines = [line.rstrip() for line in f.readlines()]

prio = 0
gprio = 0

for i, line in enumerate(lines):
    first, second = line[:len(line) // 2], line[len(line) // 2:]

    for c in first:
        if c in second:
            prio += ord(c) - ord('a' if c >= 'a' else '\'') + 1
            break
    
    if i % 3 == 0:
        for c in line:
            if c in lines[i + 1] and \
               c in lines[i + 2]:
                gprio += ord(c) - ord('a' if c >= 'a' else '\'') + 1
                break

part1 = prio
part2 = gprio

print(f'part 1: {part1}')
print(f'part 2: {part2}')
