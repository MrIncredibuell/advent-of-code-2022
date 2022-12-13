import json
from copy import deepcopy

data = [json.loads(x) for x in open('input.txt').read().split('\n') if x]

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif left > right:
            return False
        return None
    elif isinstance(left, list) and isinstance(right, list):
        if len(left) == len(right) == 0:
            return None
        if len(left) == 0:
            return True
        elif len(right) == 0:
            return False
        result = compare(left[0], right[0])
        if result is None:
            return compare(left[1:], right[1:])
        return result
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    
        

def part1(data):
    results = []
    i = 0
    while i < len(data):
        left = data[i]
        right = data[i+1]

        if compare(left, right) is True:
            results.append((i // 2) + 1)

        i += 2
    return sum(results)

def part2(data):
    data.append([[2]])
    data.append([[6]])
    for i in range(len(data)):
        for j in range(0, len(data) - i - 1):
            if not compare(data[j], data[j+1]):
                data[j], data[j+1] = data[j+1], data[j]
    results = []
    for ii, row in enumerate(data):
        if row == [[2]] or row == [[6]]:
            results.append(ii + 1)

    return results[0] * results[1]

print(part1(data))
print(part2(deepcopy(data)))