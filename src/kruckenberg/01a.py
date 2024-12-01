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

# create a single list where each item is an ordinal pair
pairwise = zip(sorted(first), sorted(second))

# calculate the absolute difference for each pair and sum differences
diff = 0
for f, s in pairwise:
    diff += abs(f - s)

print(diff)