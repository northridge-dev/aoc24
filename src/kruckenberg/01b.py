from utils.files import readlines

# read the input file and split by lines
pairs = readlines('01.txt')

first = []
second = []

# split each line and add int to first, second lists
for pair in pairs:
    [f, s] = pair.split()
    first.append(int(f))
    second.append(int(s))

# build a frequency map of numbers in the second list
freq = {}
for num in second:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

# compute the simlarity score: sum of each number in 
# list one multipled by frequency of num in list two
similarity = 0
for num in first:
    similarity += num * freq.get(num, 0)

print(similarity)