"""
Alters original solution by using some lib methods to:
  - split the input into two separate lists of integers
  - build a frequency map
  - calculate a similarity score *by reduction*
"""

from collections import Counter
from functools import reduce
from utils.files import readlines

# read the input file and split by lines
pairs = readlines('01.txt')

# split each line and add int to first, second lists
first, second = zip(*(map(int, pair.split()) for pair in pairs))

# build a frequency map of numbers in the second list
freq = Counter(second)

# compute the simlarity score: sum of each number in 
# list one multipled by frequency of num in list two
similarity = reduce(lambda s, n: s + n * freq.get(n, 0), first, 0)

print(similarity)