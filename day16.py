f = open('input/day16.txt')
lines = [line.rstrip() for line in f.readlines()]

import re
ints = lambda x: [int(i) for i in re.findall('-?\d+', x)]

adj, shift, flow = {}, {}, {}
for i, line in enumerate(lines):
    valve, rate, leads = line[6:8], ints(line)[0], set(line.split(' ', 9)[-1].split(', '))
    adj[valve] = leads; shift[valve] = 1 << i
    if rate > 0: flow[valve] = rate
dist = {n: {a: 1 if a in adj[n] else float('inf') for a in adj} for n in adj}

for k in dist:
    for i in dist:
        for j in dist:
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

def fw(a, b, s = 0, f = 0, ans = {}):
    ans[s] = max(ans.get(s, 0), f)
    for u in flow:
        b2 = b - dist[a][u] - 1
        if shift[u] & s or b2 < 1: continue
        fw(u, b2, s | shift[u], f + b2 * flow[u], ans)
    return ans

part1 = max(fw('AA', 30).values())

visited = fw('AA', 26)
part2 = max(v1 + v2 for k1, v1 in visited.items() \
                    for k2, v2 in visited.items() if not k1 & k2)

print(f'part 1: {part1}')
print(f'part 2: {part2}')
