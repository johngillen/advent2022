f = open('input/day05.txt')
lines = [line.rstrip() for line in f.readlines()]

def parse():
    tmp = lines[:lines.index('')]
    n = int(tmp[-1][-1])
    stacks = [[] for _ in range(n + 1)]
    for line in tmp[:-1]:
        for i in range(1, len(stacks)):
            try:
                c = line[(i - 1) * 4 + 1]
                if c != ' ':
                    stacks[i].insert(0, c)
            except:
                pass
    return stacks

stacks1 = parse()
stacks2 = parse()

for line in lines:
    if 'move' in line:
        n, src, dst = [int(n) for n in line.split() if n.isdigit()]

        [stacks1[dst].append(stacks1[src].pop()) for _ in range(n)]
        stacks2[dst].extend(stacks2[src][-n:])
        stacks2[src] = stacks2[src][:-n]

part1 = ''.join(stacks1[n][-1] for n in range(1, len(stacks1)))
part2 = ''.join(stacks2[n][-1] for n in range(1, len(stacks2)))

print(f'part 1: {part1}')
print(f'part 2: {part2}')
