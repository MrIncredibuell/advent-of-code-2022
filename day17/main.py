data = open('input.txt').read()

ROCK_SHAPES = [
    {(0,0), (1,0), (2,0), (3,0)},
    {(0,1), (1,2), (1,1), (1,0), (2, 1)},
    {(0,0), (1,0), (2,2), (2,1), (2,0)},
    {(0,3), (0,2), (0,1), (0,0)},
    {(0,0), (0,1), (1,0), (1,1)}
]

def print_state(state):
    max_y = max(y for x, y in state)
    while max_y:
        row  = ''
        for x in range(7):
            if (x, max_y) in state:
                row += '#'
            else:
                row += '.'
        print(row)
        max_y -= 1
    print()


def part1(data):
    objects = {(i, 0) for i in range(7)}
    starting_height = 4

    lava_index = 0

    for rock_index in range(2022):
        rock_shape = ROCK_SHAPES[rock_index % len(ROCK_SHAPES)]
        y = starting_height
        x = 2

        falling = True
        while falling:
            lava_direction = data[lava_index]
            if lava_direction == '<':
                if x == 0 or any((i + x - 1, j + y) in objects for (i, j) in rock_shape):
                    pass
                else:
                    x -= 1
            else:
                if max(i + x for (i, _) in rock_shape) >= 6 or any((i + x + 1, j + y) in objects for (i, j) in rock_shape):
                    pass
                else:
                    x += 1
            lava_index = (lava_index + 1) % len(data)

            if any((i + x, j + y - 1) in objects for (i, j) in rock_shape):
                falling = False
                objects |= {(i + x, j + y) for (i, j) in rock_shape}
            else:
                y -= 1

        starting_height = max(starting_height, *(y + j + 4 for _, j in rock_shape))

    return starting_height - 4


        

def part2(data):
    elves = sorted([sum(elf) for elf in data])
    return sum(elves[-3:])

print(part1(data))
# print(part2(data))