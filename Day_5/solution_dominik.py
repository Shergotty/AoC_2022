#!/usr/bin/env python3
import re
import numpy as np

filename = "debug.txt"


import os
in_file = os.path.relpath(f'input/{filename}')


def load_input_list():
    with open(in_file, 'r') as f:
        return [line.rstrip('\n') for line in f]

def read_input_text():
    with open(in_file, 'r') as fh:
        return fh.read().strip()

def format_input():
    complete_input = load_input_list()
    stack = complete_input[:complete_input.index("") - 1]
    movements = complete_input[complete_input.index("") + 1:]
    # format crate stacks
    max_len = 0
    for i, n in enumerate(stack):
        stack[i] = n.replace("    ", "[0]").replace(" ", "").replace("[", "").replace("]", "")
        if len(stack[i]) > max_len:
            max_len = len(stack[i])
    # make stacks all same height
    for i, n in enumerate(stack):
        if len(n) != max_len:
            stack[i] += "0"
    for i, n in enumerate(stack):
        stack[i] = list(n)
    # use np array to transpose rows to columns
    stack_arr = np.asarray(stack, dtype=object).T
    stack_dict = dict(enumerate(stack_arr.sum(axis=1)))

    # format movements
    move_pattern = r"\d+"
    move_list = []
    for move in movements:
        move_list.append([int(match) for match in re.findall(move_pattern, move)])

    return stack_dict, move_list

def move_box(stack_dict,nr_of_crates, o, d):
    # get initial stack a box
    orig_col = stack_dict[o - 1].lstrip("0")
    crate_to_move = orig_col[:nr_of_crates]

    # get destination stack
    dest_col = stack_dict[d - 1].lstrip("0")

    # move box to destination
    orig_col = orig_col[nr_of_crates:]
    dest_col = f"{crate_to_move}{dest_col}"

    # write results back to dict
    stack_dict[o - 1] = orig_col
    stack_dict[d - 1] = dest_col
    return stack_dict

def top_crates(stack_dict):
    result_string = ""

    for stack in stack_dict.values():
        result_string += stack[0]
    return result_string

def puzzle1():
    stack_dict, move_list = format_input()
    for move in move_list:
        n,o,d=move
        for m in range(n):
            stack_dict=move_box(stack_dict,1,o,d)

    return top_crates(stack_dict)

def puzzle2():
    stack_dict, move_list = format_input()
    for move in move_list:
        n, o, d = move
        stack_dict=move_box(stack_dict,n,o,d)

    return top_crates(stack_dict)

if __name__ == '__main__':
    a = puzzle1()
    print(f"Answer to Puzzle a is a total of: {a}")
    b = puzzle2()
    print(f"Answer to Puzzle b is a total of: {b}")