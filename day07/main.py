data = open('input.txt').read().split('\n')

def recursive_size(d):
    s = 0
    for v in d.values():
        if isinstance(v, int):
            s += v
        else:
            s += recursive_size(v)
    return s

def find_values(d):
    s = 0
    for v in d.values():
        if isinstance(v, dict):
            size = recursive_size(v)
            if size <= 100000:
                s += size

            s += find_values(v)
    return s

def part1(data):
    root = {}
    cwd = []
    cwd_dict = root
    for i in range(len(data)):
        line = data[i]
        if line.startswith('$ cd '):
            dest = line[5:]
            if dest == '/':
                cwd = []
                cwd_dict = root
            elif dest == '..':
                cwd = cwd[:-1]
                cwd_dict = root
                for p in cwd:
                    cwd_dict = cwd_dict[p]
            else:
                cwd.append(dest)
                cwd_dict = cwd_dict[dest]
        elif line.startswith('$ ls'):
            i += 1
            while i < len(data) and not data[i].startswith('$'):
                ls_line = data[i]
                if ls_line.startswith('dir '):
                    path = ls_line[4:]
                    cwd_dict[path] = {}
                else:
                    size, path = ls_line.split(' ')
                    size = int(size)
                    cwd_dict[path] = size
                i += 1
    return find_values(root)


def find_min_dir_size(d, min_value):
    options = [find_min_dir_size(v, min_value) for v in d.values() if isinstance(v, dict)]
    options = [o for o in options if o is not None]
    size = recursive_size(d)
    if size > min_value:
        options.append(size)
    if options:
        return min(options)
    return None
                    

def part2(data):
    root = {}
    cwd = []
    cwd_dict = root
    for i in range(len(data)):
        line = data[i]
        if line.startswith('$ cd '):
            dest = line[5:]
            if dest == '/':
                cwd = []
                cwd_dict = root
            elif dest == '..':
                cwd = cwd[:-1]
                cwd_dict = root
                for p in cwd:
                    cwd_dict = cwd_dict[p]
            else:
                cwd.append(dest)
                cwd_dict = cwd_dict[dest]
        elif line.startswith('$ ls'):
            i += 1
            while i < len(data) and not data[i].startswith('$'):
                ls_line = data[i]
                if ls_line.startswith('dir '):
                    path = ls_line[4:]
                    cwd_dict[path] = {}
                else:
                    size, path = ls_line.split(' ')
                    size = int(size)
                    cwd_dict[path] = size
                i += 1
    current_size = recursive_size(root)

    needed_size = (30000000 - (70000000 - current_size))
    return find_min_dir_size(root, needed_size)
    

print(part1(data))
print(part2(data))