from collections import defaultdict
from itertools import groupby
import re


def get_fileinput(filename: str) -> list:
    import os
    test_file = os.path.relpath(f'input/{filename}')

    with open(test_file) as f:
        content = f.readlines()
    return [x.strip('\n') for x in content]


filename = 'debug.txt'
# filename = 'day_4_1.txt'
puzzle_list = get_fileinput(filename)


def shifter(start_shift: int, shift: int) -> set:
    return puzzle_list[0][start_shift:shift]


shifted = 0
signal = ''
shift_chunk = 4
initial_chunk = shifter(shifted, shift_chunk+shifted)
shift_list = []
while shifted < len(puzzle_list[0])-shift_chunk:
    shift = shifter(shifted, shift_chunk+shifted)
    signal = f'{signal}{puzzle_list[0][4+shifted]}'
    shifted += 1
    shift_list.append(shift)

shift_list = [signal for signal in shift_list]

print(shift_list)