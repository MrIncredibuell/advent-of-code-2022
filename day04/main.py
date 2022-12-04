rows = open('input.txt').read().split('\n')
data = []
for row in rows:
    a, b = row.split(',')
    w, x = a.split('-')
    y, z = b.split('-')
    data.append([int(i) for i in [w,x,y,z]])

def part1(data):
    c = 0
    for w, x, y, z in data:
        if w <= y and x >= z:
            c += 1
        elif w >= y and x <= z:
            c += 1
    return c

def part2(data):
    c = 0
    for w, x, y, z in data:
        if set(range(w, x + 1)) & set(range(y, z + 1)):
            c += 1
    return c

print(part1(data))
print(part2(data))