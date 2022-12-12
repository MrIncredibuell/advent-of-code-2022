rows = open('input.txt').read().split('\n')
data = {}
for y, row in enumerate(rows):
    for x, v in enumerate(row):
        data[(x,y)] = v
        
def print_dists(dists):
    width, height = max(dists.keys())
    for y in range(height + 1):
        row = ''
        for x in range(width + 1):
            row = row + str('X' if (x,y) in dists else ' ')
        print(row)



def part1(data):
    edges = {}
    for (x,y), v in data.items():
        if v == 'S':
            v = 'a'
            S = (x,y)
        elif v == 'E':
            v = 'z'
            E = (x,y)
        edges[(x,y)] = set()
        for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if ((x + dx, y + dy) in data) and ord(data[(x + dx, y + dy)] if data[(x + dx, y + dy)] != 'E' else 'z' ) - ord(v) <= 1:
                edges[(x,y)].add((x + dx, y + dy))

    visited = {S: 0}
    to_visit = {n: 1 for n in edges[S]}
    while to_visit:
        dist, current = min((dist, dest) for dest, dist in to_visit.items())
        del to_visit[current]
        visited[current] = dist

        for edge in edges[current]:
            if edge in visited:
                continue
            if edge not in to_visit:
                to_visit[edge] = dist + 1
            to_visit[edge] = min(dist + 1, to_visit[edge])

    return visited[E]

def part2(data):
    edges = {}
    for (x,y), v in data.items():
        if v == 'S':
            v = 'a'
            S = (x,y)
        elif v == 'E':
            v = 'z'
            E = (x,y)
        edges[(x,y)] = set()
        for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if ((x + dx, y + dy) in data) and ord(data[(x + dx, y + dy)] if data[(x + dx, y + dy)] != 'E' else 'z' ) - ord(v) <= 1:
                edges[(x,y)].add((x + dx, y + dy))

    visited = {k: 0 for k, v in data.items() if v == 'a'}
    to_visit = {}
    for k in visited:
        for n in edges[k]:
            if n not in visited:
                to_visit[n] = 1

    while to_visit:
        dist, current = min((dist, dest) for dest, dist in to_visit.items())
        del to_visit[current]
        visited[current] = dist

        for edge in edges[current]:
            if edge in visited:
                continue
            if edge not in to_visit:
                to_visit[edge] = dist + 1
            to_visit[edge] = min(dist + 1, to_visit[edge])

    return visited[E]

print(part1(data))
print(part2(data))