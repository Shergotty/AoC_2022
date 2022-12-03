from collections import defaultdict
import string


def get_fileinput(filename: str) -> list:
    import os
    test_file = os.path.relpath(f'input/{filename}')

    with open(test_file) as f:
        content = f.readlines()
    return [x.strip() for x in content]


def create_simple_dict(char_list):

    alphabet = defaultdict(list)

    for character in char_list:
        alphabet[character].append(char_list.index(character)+1)

    for key, value in alphabet.items():
        alphabet[key] = value[0]

    return alphabet


def calc_value(letter_list: list) -> int:
    return [alphabet[list(i)[0]] for i in letter_list]


def get_common_item(list_in: list):

    splitted_items = []

    for items in list_in:
        splitted_items.append([set(item) for item in items])

    return [set.intersection(*splitted_item) for splitted_item in splitted_items]

# https://grabthiscode.com/python/split-list-on-every-nth-element-python


def chunks(list_in, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(list_in), n):
        # Create an index range for l of n items:
        yield list_in[i:i+n]


def part_1():
    backpacks = [
        [[*i][len(i)//2:], [*i][:len(i)//2]]
        for i in puzzle_list
    ]

    backpacks = get_common_item(backpacks)
    shared_items = calc_value(backpacks)

    return sum(shared_items)


def part_2():

    backpacks = list(chunks(puzzle_list, 3))
    backpacks = get_common_item(backpacks)
    shared_items = calc_value(backpacks)

    return sum(shared_items)


lower_alphabet = list(string.ascii_lowercase)
upper_alphabet = list(string.ascii_uppercase)
joined_alphabet = lower_alphabet+upper_alphabet

alphabet = create_simple_dict(joined_alphabet)

filename = 'day_3_1.txt'

# filename = 'debug'

puzzle_list = get_fileinput(filename)

print(part_1())
print(part_2())
