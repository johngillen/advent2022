f = open('input/day13.txt')
lines = [line.rstrip() for line in f.readlines()]

part1 = 0
part2 = 0

def compare(left, right):
    if type(left) == int and type(right) == int:
        if left == right:
            return None
        return left < right
    if type(left) == list and type(right) == list:
        for l, r in zip(left, right):
            result = compare(l, r)
            if result is not None:
                return result
        if len(left) == len(right):
            return None
        return len(left) < len(right)

    if type(left) == list and type(right) == int:
        return compare(left, [right])
    if type(left) == int and type(right) == list:
        return compare([left], right)

def packetmin(packets):
    result = packets[0]
    for packet in packets:
        if compare(packet, result):
            result = packet
    return result

lines = [eval(line) for line in lines if line != '']
for i in range(0, len(lines), 2):
    part1 += i // 2 + 1 if compare(lines[i], lines[i + 1]) else 0
lines.extend([[[2]], [[6]]])
for i in range(len(lines)):
    lines.insert(i, lines.pop(lines.index(packetmin(lines[i:]))))

part2 = (lines.index([[2]]) + 1) * (lines.index([[6]]) + 1)

print(f'part 1: {part1}')
print(f'part 2: {part2}')
