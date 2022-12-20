f = open('input/day20.txt')
lines = [line.rstrip() for line in f.readlines()]

def mix(list, rounds):
    l2 = [(i, n) for i, n in enumerate(list)]
    for _ in range(rounds):
        for i, n in enumerate(list):
            j = l2.index((i, n)); k = l2.pop(j)
            if (j + n) == 0: l2.append(k); continue
            l2.insert((j + n) % len(l2), k)
    return [n for _, n in l2]

mixsum = lambda l: sum([l[(l.index(0) + i) % len(l)] \
                       for i in [1000, 2000, 3000]])

part1 = mixsum(mix([int(l) for l in lines], 1))
part2 = mixsum(mix([int(l) * 811589153 for l in lines], 10))

print(f'part 1: {part1}')
print(f'part 2: {part2}')
