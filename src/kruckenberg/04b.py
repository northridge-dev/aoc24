import re
from utils.files import readlines

# get crossword rows
rows = readlines('04.txt')

# strategy: enumerate all the patterns that could exist 
# at a given position in row and row + 2 (row + 1 should 
# always be 'A' offset to the right by 1)
patterns = [
    (r'(?=(M.M))', r'S.S'),
    (r'(?=(M.S))', r'M.S'),
    (r'(?=(S.M))', r'S.M'),
    (r'(?=(S.S))', r'M.M'),
]

count = 0


for idx, row in enumerate(rows[:-2]): # no need to iter through last two rows because pattern is three rows
    for pattern in patterns:
        first, third = pattern
        matches = re.finditer(first, row)
        for match in matches:
            start = match.start()
            if (
                rows[idx + 1][start + 1] == 'A' 
                and re.match(third, rows[idx + 2][start:start + 3])
            ):
                count += 1 

print(count)