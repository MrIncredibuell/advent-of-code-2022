data = open('input.txt').read()

def part1(data):
    for i in range(4, len(data) + 1):
        if len(set(data[i-4:i])) == 4:
            return i

def part2(data):
    for i in range(14, len(data) + 1):
        if len(set(data[i-14:i])) == 14:
            return i

print(part1(data))
print(part2(data))