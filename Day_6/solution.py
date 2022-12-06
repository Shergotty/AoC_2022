def get_fileinput(filename: str) -> list:
    import os
    test_file = os.path.relpath(f'input/{filename}')

    with open(test_file) as f:
        content = f.readlines()
    return [x.strip('\n') for x in content]

def shifter(code_in, start_shift: int, shift: int) -> set:
    return code_in[start_shift:shift]

def get_first_signal(code_in:str, shift_chunk:int)-> int:

    shifted = 0
    signal = ''
    shift_list = []
    while shifted < len(code_in)-shift_chunk:
        shift = shifter(code_in, shifted, shift_chunk+shifted)
        signal = f'{signal}{code_in[4+shifted]}'
        shifted += 1
        shift_list.append(shift)
    
    shift_list = [signal for signal in shift_list]
    
    return shift_chunk+[shift_list.index(i) for i in shift_list if len(set(i)) == shift_chunk][0]


filename = 'debug.txt'
filename = 'day_6_1.txt'
puzzle_list = get_fileinput(filename)
a,b = [[get_first_signal(code_in, shift_chunk) for code_in in puzzle_list] for shift_chunk in [4, 14]]
print(a,b)