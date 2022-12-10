data = open('input.txt').read().split('\n')

def parse_instruction(row):
    if row == 'noop':
        return None
    else:
        inst, value = row.split(' ')
        return inst, int(value)

def part1(data):
    x = 1
    results = []
    i = 1
    for instruction in data:
        instruction = parse_instruction(instruction)
        if i % 40 == 20:
            results.append(i * x)

        if instruction:
            i +=1
            _, value = instruction
            if i % 40 == 20:
                results.append(i * x)
            x += value
        else:
            pass
        i += 1
    return sum(results)

def part2(data):
    x = 1
    results = []
    i = 0
    for instruction in data:
        instruction = parse_instruction(instruction)

        if -1 <= (i % 40) - x <= 1:
            results.append('#')
        else:
            results.append('.')

        if instruction:
            i +=1
            _, value = instruction
            if -1 <= (i % 40) - x <= 1:
                results.append('#')
            else:
                results.append('.')
            x += value
        else:
            pass
        i += 1
    result = ''
    for y in range(6):
        result += ''.join(results[y * 40: (y+1)*40]) + '\n'
    return result

print(part1(data))
print(part2(data))