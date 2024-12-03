import os 

def getFilePath(inputFile):
    LASTNAME = os.environ.get('LASTNAME')
    input_dir = f"/workspaces/aoc24/src/{LASTNAME}/input"
    return os.path.join(input_dir, inputFile)

def readfile(inputFile):
    path_to_input = getFilePath(inputFile)
    try:
        with open(path_to_input) as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"{inputFile} not found")
        return ''

def readlines(inputFile):
    path_to_input = getFilePath(inputFile)
    try:
        with open(path_to_input) as file:
            lines = [line.rstrip() for line in file]
        return lines
    except FileNotFoundError:
        print(f"{inputFile} not found")
        return []