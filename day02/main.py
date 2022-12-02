data = [row.split(' ') for row in open('input.txt').read().split('\n')]

input_map = {
    'A': 'ROCK',
    'B': "PAPER",
    'C': 'SCISSORS',
    'X': 'ROCK',
    'Y': "PAPER",
    'Z': 'SCISSORS',
}

values = ['ROCK', 'PAPER', 'SCISSORS']

def part1(data):
    score = 0
    for them, me in data:
        me = input_map[me]
        them = input_map[them]
        score += values.index(me) + 1
        me_index = values.index(me)
        them_index =  values.index(them)
        if (me_index - 1) % 3 == them_index:
            score += 6
        elif me_index == them_index:
            score += 3
    return score

results = {
    'X': 'LOSE',
    'Y': 'DRAW', 
    'Z': 'WIN',
}

def part2(data):
    score = 0
    for them, result in data:
        result = results[result]
        them = input_map[them]
        if result == 'WIN':
            score += 6 + (values.index(them) + 1) % 3 + 1
        elif result == 'DRAW':
            score += 3 + (values.index(them)) % 3 + 1
        elif result == 'LOSE':
            score += (values.index(them) - 1) % 3 + 1
    return score

print(part1(data))
print(part2(data))