from collections import defaultdict
import string


def get_fileinput(filename: str) -> list:
    import os
    test_file = os.path.abspath(f'input/{filename}')

    with open(test_file) as f:
        content = f.readlines()
    return [x.strip() for x in content]


def create_simple_dict(char_list, alphabet_dict_in):

    for character in char_list:
        alphabet_dict_in[char_list.index(character)+1].append(character)


def part_1_dict():

    part_1_dict = alphabet_dict
    create_simple_dict(alphabet[:3], part_1_dict)
    create_simple_dict(alphabet[-3:], part_1_dict)

    return part_1_dict


def rps(pair_list, dict_in):
    rps_dict = {
        1: 'rock',  2: 'paper', 3: 'scissors'
    }

    weakness = {
        'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'
    }

    for key, value in rps_dict.items():
        rps_dict[key] = {value: dict_in[key]}

    result_list = []

    for i in pair_list:
        for key, value in rps_dict.items():
            for sub_key, subvalue in value.items():
                if i in subvalue:
                    result_list.append([key, sub_key, weakness[sub_key]])

    if result_list[1][1] == result_list[0][1]:
        result = result_list[1][0] + 3
    elif result_list[1][2] == result_list[0][1]:
        result = result_list[1][0]
    else:
        result = result_list[1][0] + 6

    return result


def rps_2(pair_list):

    rps_dict = {
        'rock': ['a', 1],  'paper': ['b', 2], 'scissors': ['c', 3]
    }

    strength = {
        'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'
    }

    weakness = {
        'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'
    }

    for key, value in rps_dict.items():
        if pair_list[1] == 'z' and pair_list[0] in value:
            result = rps_dict[weakness[key]][1] + 6
        elif pair_list[1] == 'x' and pair_list[0] in value:
            result = rps_dict[strength[key]][1]
        elif pair_list[1] == 'y' and pair_list[0] in value:
            result = value[1] + 3

    return result


alphabet = list(string.ascii_lowercase)

alphabet_dict = defaultdict(list)


filename = 'day_2_1.txt'

# filename = 'debug'


puzzle_list = get_fileinput(filename)

puzzle_pairs = [element.lower().split(' ') for element in puzzle_list]

part_1_dict = part_1_dict()

result_part_1 = sum([rps(pair, part_1_dict) for pair in puzzle_pairs])

result_part_2 = sum([rps_2(pair) for pair in puzzle_pairs])

print(result_part_1, result_part_2)
