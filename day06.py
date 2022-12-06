f = open('input/day06.txt')
lines = [line.rstrip() for line in f.readlines()]

part1 = None
part2 = None

packet = []
message = []

for line in lines:
    for i, c, in enumerate(line):
        if i >= 4:
            if part1 is None and sorted(packet) == sorted(set(packet)):
                part1 = i
            else:
                packet.pop(0)
        if i >= 14:
            if part2 is None and sorted(message) == sorted(set(message)):
                part2 = i
            else:
                message.pop(0)
        packet.append(c)
        message.append(c)

print(f'part 1: {part1}')
print(f'part 2: {part2}')
