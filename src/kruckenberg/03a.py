import re
from utils.files import readfile

corrupted = readfile('03.txt')
mul_pattern = r'mul\(\d+,\d+\)'

matches = re.findall(mul_pattern, corrupted)

def get_and_mult_factors(mulString):
    first, second = re.search(r'\d+,\d+', mulString).group().split(',')
    return int(first) * int(second)

print(sum(map(get_and_mult_factors, matches)))