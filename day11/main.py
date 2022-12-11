from copy import deepcopy

monkeys = open('input.txt').read().split('\n\n')

def parse_monkey(rows):
    monkey = {}
    monkey['items'] = [int(x) for x in rows[1][len('  Starting items: '):].split(', ')]
    monkey['operator'], monkey['operand'] = rows[2][len('  Operation: new = old '):].split(' ')
    try:
        monkey['operand'] = int(monkey['operand'])
    except:
        pass
    monkey['test'] = int(rows[3][len('  Test: divisible by '):])
    monkey['if_true'] = int(rows[4][len('    If true: throw to monkey '):])
    monkey['if_false'] = int(rows[5][len('    If false: throw to monkey '):])
    return monkey

data = [parse_monkey(monkey.split('\n')) for monkey in monkeys]

def part1(data):
    monkeys = deepcopy(data)
    counts = {i: 0 for i in range(len(monkeys))}
    for _ in range(20):
        for i, monkey in enumerate(monkeys):
            for item in monkey['items']:
                counts[i] += 1
                if monkey['operand'] == 'old':
                    operand = item
                else:
                    operand = monkey['operand']
                if monkey['operator'] == '+':
                    inspect = item + operand
                elif monkey['operator'] == '*':
                    inspect = item * operand
                else:
                    raise Exception(f'unknown operator {monkey["operator"]}')
                
                worry = inspect // 3
                if worry % monkey['test'] == 0:
                    monkeys[monkey['if_true']]['items'].append(worry)
                else:
                    monkeys[monkey['if_false']]['items'].append(worry)
                monkey['items'] = monkey['items'][1:]
    # for i, monkey in enumerate(monkeys):
    #     print(i, monkey['items'])
    counts = sorted(counts.values())
    return counts[-1] * counts[-2]

def part2(data):
    monkeys = deepcopy(data)
    counts = {i: 0 for i in range(len(monkeys))}

    divisors = [monkey['test'] for monkey in monkeys]
    for monkey in monkeys:
        new_items = []
        for item in monkey['items']:
            new_item = {}
            for divisor in divisors:
                new_item[divisor] = item % divisor
            new_items.append(new_item)
        monkey['items'] = new_items

    for _ in range(10000):
        for i, monkey in enumerate(monkeys):
            for item in monkey['items']:
                counts[i] += 1
                if monkey['operand'] == 'old':
                    operand = item
                else:
                    operand = {k: monkey['operand'] for k in item.keys()}
                if monkey['operator'] == '+':
                    new_item = {
                        k: (v + operand[k]) % k for k, v in item.items()
                    }
                elif monkey['operator'] == '*':
                    new_item = {
                        k: (v * operand[k]) % k for k, v in item.items()
                    }
                else:
                    raise Exception(f'unknown operator {monkey["operator"]}')
                if new_item[monkey['test']] == 0:
                    monkeys[monkey['if_true']]['items'].append(new_item)
                else:
                    monkeys[monkey['if_false']]['items'].append(new_item)
                monkey['items'] = monkey['items'][1:]

    counts = sorted(counts.values())
    return counts[-1] * counts[-2]

print(part1(data))
print(part2(data))