rows = open('input.txt').read().split('\n')

data = []
for row in rows:
    direction, magnitude = row.split(' ')
    data.append((direction, int(magnitude)))

def move_tail(hx, hy, tx, ty):
    new_tx = tx
    new_ty = ty
    delta_x = hx - tx
    delta_y = hy - ty

    if abs(delta_x) > 1 and abs(delta_y) > 1:
        new_tx += delta_x / abs(delta_x)
        new_ty += delta_y / abs(delta_y)

    elif abs(delta_x) > 1 and abs(delta_y) == 1:
        new_tx += delta_x / abs(delta_x)
        new_ty = hy

    elif abs(delta_y) > 1 and abs(delta_x) == 1:        
        new_ty += delta_y / abs(delta_y)
        new_tx = hx

    elif abs(delta_x) > 1:
        new_tx += delta_x / abs(delta_x)
    elif abs(delta_y) > 1:
        new_ty += delta_y / abs(delta_y)

    return (new_tx, new_ty)


def part1(data):
    hx, hy = (0, 0)
    tx, ty = (0, 0)
    visited = set()
    for direction, magnitude in data:
        if direction == 'U':
            for _ in range(magnitude):
                hy -= 1
                tx, ty = move_tail(hx, hy, tx, ty)
                visited.add((tx, ty))
        elif direction == 'D':
            for _ in range(magnitude):
                hy += 1
                tx, ty = move_tail(hx, hy, tx, ty)
                visited.add((tx, ty))
        elif direction == 'L':
            for _ in range(magnitude):
                hx -= 1
                tx, ty = move_tail(hx, hy, tx, ty)
                visited.add((tx, ty))
        elif direction == 'R':
            for _ in range(magnitude):
                hx += 1
                tx, ty = move_tail(hx, hy, tx, ty)
                visited.add((tx, ty))
    return len(visited)


def part2(data):
    hx, hy = (0, 0)
    tails = [(0, 0)] * 9
    visited = set()
    for direction, magnitude in data:
        if direction == 'U':
            for _ in range(magnitude):
                hy -= 1
                x, y = hx, hy
                for i, (tx, ty) in enumerate(tails):
                    x, y = move_tail(x, y, tx, ty)
                    tails[i] = (x,y)
                visited.add(tails[-1])
        elif direction == 'D':
            for _ in range(magnitude):
                hy += 1
                x, y = hx, hy
                for i, (tx, ty) in enumerate(tails):
                    x, y = move_tail(x, y, tx, ty)
                    tails[i] = (x,y)
                visited.add(tails[-1])
        elif direction == 'L':
            for _ in range(magnitude):
                hx -= 1
                x, y = hx, hy
                for i, (tx, ty) in enumerate(tails):
                    x, y = move_tail(x, y, tx, ty)
                    tails[i] = (x,y)
                visited.add(tails[-1])
        elif direction == 'R':
            for _ in range(magnitude):
                hx += 1
                x, y = hx, hy
                for i, (tx, ty) in enumerate(tails):
                    x, y = move_tail(x, y, tx, ty)
                    tails[i] = (x,y)
                visited.add(tails[-1])

    return len(visited)

print(part1(data))
print(part2(data))