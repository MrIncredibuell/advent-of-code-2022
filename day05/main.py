from copy import deepcopy

setup, moves = open('input.txt').read().split('\n\n')
setup = setup.split('\n')
stack_count = int(setup[-1].strip(' ').split('   ')[-1])
stacks = [[] for _ in range(stack_count)]
for i in range(len(setup) -1):
    for x in range(stack_count):
        v = setup[i][x * 4 + 1]
        if v != ' ':
            stacks[x].append(v)
stacks = [s[::-1] for s in stacks]
moves = moves.split('\n')

def part1(stacks, moves):
    for move in moves:
        move = move.replace('move ', '')
        move = move.replace(' from ', ' ')
        move = move.replace(' to ', ' ')
        c, f, t = [int(v) for v in move.split(' ')]
        for _ in range(c):
            stacks[t-1].append(stacks[f-1].pop())
    return ''.join([s[-1] for s in stacks])

def part2(stacks, moves):
    for move in moves:
        move = move.replace('move ', '')
        move = move.replace(' from ', ' ')
        move = move.replace(' to ', ' ')
        c, f, t = [int(v) for v in move.split(' ')]
        stacks[t-1].extend(stacks[f-1][-c:])
        stacks[f-1] = stacks[f-1][:-c]
        
    return ''.join([s[-1] for s in stacks])

print(part1(deepcopy(stacks), moves))
print(part2(deepcopy(stacks), moves))