f = open('input/day03.txt')
lines = [line.rstrip() for line in f.readlines()]

part1 = 0
part2 = 0

for i, line in enumerate(lines):
    for c in line[:len(line) // 2]:
        if c in line[len(line) // 2:]:
            part1 += ord(c) - ord('a' if c >= 'a' else '\'') + 1
            break
    
    if i % 3 == 0:
        for c in line:
            if c in lines[i + 1] and \
               c in lines[i + 2]:
                part2 += ord(c) - ord('a' if c >= 'a' else '\'') + 1
                break

print(f'part 1: {part1}')
print(f'part 2: {part2}')
