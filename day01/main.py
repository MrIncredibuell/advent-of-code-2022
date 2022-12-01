elves = open('input.txt').read().split('\n\n')
data = []
for elf in elves:
    data.append([int(x) for x in elf.split('\n')])

def part1(data):
    return max(sum(elf) for elf in data)
        

def part2(data):
    elves = sorted([sum(elf) for elf in data])
    return sum(elves[-3:])

print(part1(data))
print(part2(data))