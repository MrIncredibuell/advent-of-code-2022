from copy import deepcopy

rows = open('input.txt').read().split('\n')
data = {}
for row in rows:
    last_point = None
    for point in row.split(' -> '):
        x, y = point.split(',')
        x, y = int(x), int(y)
        data[(x,y)] = '#'
        if not last_point:
            last_point = (x,y)
            continue
        old_x, old_y = last_point
        
        delta_x = x - old_x
        delta_y = y - old_y

        if delta_x > 0:
            for i in range(old_x, x + 1):
                data[(i, y)] = '#'
        elif delta_x < 0:
            for i in range(x, old_x + 1):
                data[(i, y)] = '#'

        if delta_y > 0:
            for j in range(old_y, y + 1):
                data[(x, j)] = '#'
        elif delta_y < 0:
            for j in range(y, old_y + 1):
                data[(x, j)] = '#'
        last_point = (x,y)



def part1(data):
    source = (500, 0)
    max_depth = max([y for _, y  in data.keys()])
    count = 0

    ended = False
    while not ended:
        x, y = source
        falling = True
        while falling:
            if y == max_depth:
                return count
            if data.get((x, y+1), ' ') == ' ':
                y += 1
            elif data.get((x-1, y+1), ' ') == ' ':
                y += 1
                x -= 1
            elif data.get((x+1, y+1), ' ') == ' ':
                y += 1
                x += 1
            else:
                falling = False
                data[(x,y)] = 'o'

        count += 1
    
        

def part2(data):
    source = (500, 0)
    max_depth = max([y for _, y  in data.keys()])
    count = 0

    ended = False
    while not ended:
        if data.get(source, ' ') == 'o':
            return count
        x, y = source
        falling = True
        while falling:
            if y == max_depth + 1:
                falling = False
                data[(x, y)] = 'o'
            elif data.get((x, y+1), ' ') == ' ':
                y += 1
            elif data.get((x-1, y+1), ' ') == ' ':
                y += 1
                x -= 1
            elif data.get((x+1, y+1), ' ') == ' ':
                y += 1
                x += 1
            else:
                falling = False
                data[(x,y)] = 'o'

        count += 1

print(part1(deepcopy(data)))
print(part2(deepcopy(data)))