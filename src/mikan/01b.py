from utils.files import readlines
import math

inputs = readlines("01.txt")

list_1 = []
list_2 = []
for i in inputs:
    list_1.append(int(i[:5]))
    list_2.append(int(i[-5:]))

total = 0
for i in list_1:
    similarity = 0
    for n in list_2:
        if i == n:
            similarity += i
    total += similarity
print(total)