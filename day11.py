f = open('input/day11.txt')
lines = [line.rstrip() for line in f.readlines()]

from re import findall
from numpy import prod

ints = lambda x: list(map(int, findall(r'\d+', x)))

monkies = []

class monkey:
    items = []
    op = ''
    test = 0
    a, b = 0, 0
    business = 0
    
    def inspect(self, monkies, lcm=None):
        for old in self.items:
            new = eval(f'old{self.op}')
            self.business += 1

            if lcm:
                new %= lcm
            else:
                new //= 3
            
            if not new % self.test:
                monkies[self.a].items.append(new)
            else:
                monkies[self.b].items.append(new)
        self.items = []
    
    def copy(self):
        m = monkey()
        m.items = self.items[:]
        m.op = self.op
        m.test = self.test
        m.a = self.a
        m.b = self.b
        m.business = self.business
        return m

for line in lines:
    if 'Monkey' in line:
        monkies.append(monkey())
    elif 'Starting' in line:
        monkies[-1].items = ints(line)
    elif 'Operation' in line:
        monkies[-1].op = ''.join(line.split()[-2:])
    elif 'Test' in line:
        monkies[-1].test = ints(line)[0]
    elif 'If true' in line:
        monkies[-1].a = ints(line)[0]
    elif 'If false' in line:
        monkies[-1].b = ints(line)[0]

part1 = [m.copy() for m in monkies]
part2 = [m.copy() for m in monkies]

for round in range(20):
    for m in part1:
        m.inspect(part1)

lcm = prod([m.test for m in monkies])
for round in range(10000):
    for m in part2:
        m.inspect(part2, lcm)

part1 = prod(sorted([m.business for m in part1])[-2:])
part2 = prod(sorted([m.business for m in part2])[-2:])

print(f'part 1: {part1}')
print(f'part 2: {part2}')
