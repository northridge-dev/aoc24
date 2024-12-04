from utils.files import readlines
import math

inputs = readlines("01.txt")

list_1 = []
list_2 = []
for i in inputs:
    list_1.append(int(i[:5]))
    list_2.append(int(i[-5:]))

list_1 = sorted(list_1)
list_2 = sorted(list_2)
total = 0
for i in range(len(inputs)):
    diff = list_1[i] - list_2[i]
    if diff < 0:
        diff *= -1
    total += diff
print(total)