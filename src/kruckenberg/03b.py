import re
from utils.files import readfile

corrupted = readfile('03.txt')
print(corrupted)
mul_pattern = r'mul\(\d+,\d+\)'
strip_pattern = rf"do\(\)|don\'t\(\)|{mul_pattern}"
do = 'do()'
dont = "don't()"

matches = re.findall(strip_pattern, corrupted)

enabled = True
total = 0
count = 0
for match in matches:
    if match == do:
        enabled = True
    elif match == dont:
        enabled = False
    elif re.match('mul', match):
        if enabled:
            count += 1
            factor1, factor2 = re.search(r'\d+,\d+', match).group().split(',')
            total += int(factor1) * int(factor2)
    
print(count)
print(total)
