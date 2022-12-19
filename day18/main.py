rows = [x.split(',') for x in open('input.txt').read().split('\n')]
data = []
for row in rows:
    data.append(tuple(int(x) for x in row))


def part1(data):
    nodes = set(data)
    faces_count = 0
    for (x, y, z) in nodes:
        faces_count += len([p for p in [
            (x + 1, y, z),
            (x - 1, y, z),
            (x, y + 1, z),
            (x, y - 1, z),
            (x, y, z + 1),
            (x, y, z - 1),
        ] if p not in nodes])
    return faces_count
        

def part2(data):
    nodes = set(data)
    to_visit = set([(0,0,0)])
    visited = set()

    faces_count = 0

    while to_visit:
        x, y, z = to_visit.pop()
        visited.add((x,y,z))
        neighbors = {
            (x + 1, y, z),
            (x - 1, y, z),
            (x, y + 1, z),
            (x, y - 1, z),
            (x, y, z + 1),
            (x, y, z - 1),
        }

        neighbors = {node for node in neighbors if max(node) <= 21 and min(node) >= -1}
        faces_count += len(neighbors.intersection(nodes))
        neighbors -= nodes
        neighbors -= visited
        to_visit |= neighbors
    return faces_count


print(part1(data))
print(part2(data))