# read in the file
from utils.files import readlines
lines = readlines('01.txt')

# split the columns into lists
list_one = []
list_two = []

for line in lines:
    left, right = line.split()
    list_one.append(int(left))
    list_two.append(int(right))

# sort the lists
list_one.sort()
list_two.sort()


# find the difference for each pair
# add the differences
total = 0
for index in range(len(list_one)):
    left_value = list_one[index]
    right_value = list_two[index]
    total = total + abs(left_value - right_value)

print(total)