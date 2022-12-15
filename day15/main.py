from collections import defaultdict

rows = open('input.txt').read().split('\n')
data = []
for row in rows:
    sensor, beacon = row[len('Sensor at '):].split(': closest beacon is at ')
    sx, sy = sensor.split(', ')
    bx, by = beacon.split(', ')
    data.append((int(sx[2:]),int(sy[2:]), int(bx[2:]), int(by[2:])))


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def part1(data):
    j = 2000000
    xs = []
    bxs = set()

    for sx, sy, bx, by in data:
        if by == j:
            bxs.add(bx)
        distance = dist(sx, sy, bx, by)
        dj = abs(sy - j)
        dx = distance - dj
        if dx >= 0:
            xs.append((sx - dx, sx + dx))
    
    xs = sorted(xs)
    start = xs[0][0]
    end = xs[0][1]
    count = 0
    overlapping_beacons = set()
    i = 0
    for x1, x2 in xs[1:]:
        if x1 <= end:
            end = max(x2, end)
        else:
            count += end - start + 1
            for bx in bxs:
                if start <= bx <= end:
                    overlapping_beacons.add(bx)
            start = x1
            end = x2

    count += end - start + 1

    for bx in bxs:
        if start <= bx <= end:
            overlapping_beacons.add(bx)

    return count - len(overlapping_beacons)


def part2(data):

    for j in range(4000000 + 1):
        xs = []

        for sx, sy, bx, by in data:
            distance = dist(sx, sy, bx, by)
            dj = abs(sy - j)
            dx = distance - dj
            if dx >= 0:
                xs.append((sx - dx, sx + dx))
        
        xs = sorted(xs)
        end = xs[0][1]

        for x1, x2 in xs[1:]:
            if x1 <= end:
                end = max(x2, end)
            else:
                if x1 - 1 > end:
                    print(x1, j)
                    return (x1 - 1) * 4000000 + j
                end = x2


print(part1(data))
print(part2(data))