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

    work = False
    for n in range(len(list_of_nums)):
        test = True
        new_list = list_of_nums.copy()
        new_list.pop(n)
        increase = None
        for x in range(len(new_list)-1):
            diff = new_list[x] - new_list[x+1]
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
            work = True
    if work == True:
        answer += 1

print(answer)