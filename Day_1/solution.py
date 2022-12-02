def get_fileinput(filename: str) -> list:
    import os
    test_file = os.path.relpath(f'input/{filename}')
    
    with open(test_file) as f:
        content = f.readlines()
    return [x.strip() for x in content]

def get_list(p_input: list) -> list:
    return [sum(map(int,sublist)) for sublist in p_input if p_input != '']

def puzzle_1(l_input: list) -> int:
    return max(get_list(l_input))

def puzzle_2(l_input: list) -> int:
    top_3 = sorted(get_list(l_input))[-3:]
    return sum(top_3)

filename = 'day_1_1.txt'

puzzle_list = get_fileinput(filename)

from itertools import groupby

splitted_list = [list(sub) for ele, sub in groupby(puzzle_list, key = bool) if ele]

print(puzzle_1(splitted_list))

print(puzzle_2(splitted_list))