data = open('input.txt').read().split('\n')

def part1(data):
    doubles = []
    for row in data:
        split_point = len(row) // 2
        a = row[:split_point]
        b = row[split_point:]
        for c in a:
            if c in b:
                doubles.append(c)
                break
    v = 0
    for c in doubles:
        if c.isupper():
            v += 27 + ord(c) - ord('A')
        else:
            v += 1 + ord(c) - ord('a')
    return v


def part2(data):
    i = 0
    items = []
    while i < len(data):
        m = set(data[i]) & set(data[i+1]) & set(data[i+2])
        items.append(m.pop())
        i += 3

    v = 0
    for c in items:
        if c.isupper():
            v += 27 + ord(c) - ord('A')
        else:
            v += 1 + ord(c) - ord('a')
    return v

print(part1(data))
print(part2(data))