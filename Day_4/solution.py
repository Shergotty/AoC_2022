def get_fileinput(filename: str) -> list:
    import os
    test_file = os.path.relpath(f'input/{filename}')

    with open(test_file) as f:
        content = f.readlines()
    return [x.strip() for x in content]

def get_ranges(linst_input: list) -> list:

    pairs = [pair.split(',') for pair in linst_input]
    return [[list(map(int, i.split('-'))) for i in p] for p in pairs]

def ranger(list_input: list) -> range:
    return range(list_input[0], list_input[-1]+1, 1)

def set_comparer_a(list_input: list) -> int:

    counter = 0
    if set(list_input[0]).issubset(list_input[1]) or set(list_input[1]).issubset(list_input[0]):
        counter += 1
    return counter

def set_comparer_b(list_input: list) -> int:

    counter = 0
    if set(list_input[0]).intersection(list_input[1]) or set(list_input[1]).intersection(list_input[0]):
        counter += 1
    return counter

def get_range_pairs(list_input: list) -> list:
    
    prepared_pairs = [pairs for pairs in list_input]
    a,b = [[func([ranger(p) for p in pair]) for pair in prepared_pairs] for func in [set_comparer_a, set_comparer_b]]
    return a, b

# filename = 'debug'
filename = 'day_4_1.txt'
puzzle_list = get_fileinput(filename)
ranges = get_ranges(puzzle_list)
print([sum(i) for i in get_range_pairs(ranges)])