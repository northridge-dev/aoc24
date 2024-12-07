import re
import numpy as np
from utils.files import readlines

# get crossword rows
rows = readlines('04.txt')


# get crossword columns
rows_split = [list(r) for r in rows]
cols = []
for i in range(len(rows_split[0])):
    curr_col = []
    for row in rows_split:
        curr_col.append(row[i])
    cols.append("".join(curr_col))

# get crossword diagonals
diagonals = []
matrix = np.array(rows_split)
flipped_matrix = np.fliplr(matrix)
inverted_matrix = np.flipud(matrix)
inverted_flipped_matrix = np.flipud(flipped_matrix)

for offset in range(len(rows_split[0])):
    diagonals.append("".join(matrix.diagonal(offset=offset).tolist()))
    diagonals.append("".join(flipped_matrix.diagonal(offset=offset).tolist()))
    if offset > 0:
        diagonals.append("".join(inverted_matrix.diagonal(offset=offset).tolist()))
        diagonals.append("".join(inverted_flipped_matrix.diagonal(offset=offset).tolist()))


# count XMAS and SAMX matches in all rows, columns, and diagonals
count = 0

for run in rows + cols + diagonals:
    matches = re.findall(r'XMAS', run) + re.findall(r'SAMX', run)
    count += len(matches)

print(count)