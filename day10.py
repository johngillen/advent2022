f = open('input/day10.txt')
lines = [line.rstrip() for line in f.readlines()]

c, x, q = 0, 1, [0]
signal = 0
crt = [['' for _ in range(40)] for _ in range(6)]

def instruction(val):
    global c, x, q, crt, signal
    q.insert(0, val)
    crt[c // 40][c % 40] = '█' if abs((c % 40) - x) < 2 else ' '
    c += 1
    signal += c * x if c in [20, 60, 100, 140, 180, 220] else 0
    x += q.pop()

for line in lines:
    if 'addx' in line:
        instruction(int(line.split()[-1]))
    instruction(0)

part1 = signal

print(f'part 1: {part1}')
print(f'part 2: ')
[print(''.join(r)) for r in crt]
