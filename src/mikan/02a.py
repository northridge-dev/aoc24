from utils.files import readlines
import math

inputs = readlines("02.txt")

answer = 0

for i in inputs:
    num = ''
    list_of_nums = []
    counter = 0
    for n in i:
        counter +=1
        if n == ' ' and num != '':
            num = int(num)
            list_of_nums.append(num)
            num = ''
        elif n != ' ':
            num += n
    num = int(num)
    list_of_nums.append(num)
    num = ''

    test = True
    increase = None
    for x in range(len(list_of_nums)-1):
        diff = list_of_nums[x] - list_of_nums[x+1]
        if increase == None:
            if diff > 0:
                increase = True
            else:
                increase = False
    
        if increase == True and diff > 0 and diff < 4:
            pass
        elif increase == False and diff < 0 and diff > -4:
            pass
        else:
            test = False

    if test == True:
        answer += 1

print(answer)
