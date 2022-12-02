def get_fileinput(filename: str) -> list:
    import os
    test_file = os.path.abspath(f'input/{filename}')
    
    with open(test_file) as f:
        content = f.readlines()
    return [x.strip() for x in content]


# print('test')