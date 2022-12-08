data = {}

rows = open('input.txt').read().split('\n')
for y, row in enumerate(rows):
    for x, height in enumerate(row):
        data[(x, y)] = int(height)

def part1(data):
    width, height = max(data.keys())
    width += 1
    height += 1
    visible = set()
    for i in range(width):
        cur = -1
        for j in range(height):
            if data[(i,j)] > cur:
                cur = data[(i,j)]
                visible.add((i,j))
        cur = -1
        for j in range(height-1, -1, -1):
            if data[(i,j)] > cur:
                cur = data[(i,j)]
                visible.add((i,j))

    for j in range(height):
        cur = -1
        for i in range(width):
            if data[(i,j)] > cur:
                cur = data[(i,j)]
                visible.add((i,j))
        cur = -1
        for i in range(width-1, -1, -1):
            if data[(i,j)] > cur:
                cur = data[(i,j)]
                visible.add((i,j))
    return len(visible)

def part2(data):
    width, height = max(data.keys())
    width += 1
    height += 1

    best = -1
    for x in range(width):
        for y in range(height):
            score = []
        
            cur = data[x,y]
            cur_score = 0
            for i in range(x-1, -1, -1):
                cur_score += 1
                if data[(i,y)] >= cur:
                    break
            score.append(cur_score)

            cur_score = 0
            for i in range(x+1, width):
                cur_score += 1
                if data[(i,y)] >= cur:
                    break
            score.append(cur_score)

            cur_score = 0
            for j in range(y-1, -1, -1):
                cur_score += 1
                if data[(x,j)] >= cur:
                    break
            score.append(cur_score)

            cur_score = 0
            for j in range(y+1, height):
                cur_score += 1
                if data[(x,j)] >= cur:
                    break
            score.append(cur_score)
            
            v = score[0] * score[1] * score[2] * score[3]

            if v > best:
                best = v  
    return best

print(part1(data))
print(part2(data))