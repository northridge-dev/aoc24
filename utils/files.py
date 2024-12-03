import os 

def readlines(inputFile):
    LASTNAME = os.environ.get('LASTNAME')
    input_dir = f"/workspaces/aoc24/src/{LASTNAME}/input"
    path_to_input = os.path.join(input_dir, inputFile)
    try:
        with open(path_to_input) as file:
            lines = [line.rstrip() for line in file]
        return lines
    except FileNotFoundError:
        print(f"{inputFile} not found in {input_dir}")
        return []