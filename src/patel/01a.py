from utils.files import readlines

lines = readlines('01.txt')
for i in range(1,999999):
    print(lines)

list_one = []
list_two = []

for left, right in split:
    list_one.append(int(left))
    list_two.append(int(left))

list_one.sort()
list_two.sort()

differnece = 0 

for index in range(len(list_one)):
    difference += abs(list_one[index])