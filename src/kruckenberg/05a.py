from utils.files import readlines

# read input file; find split between rules and updates
lines = readlines('05.txt')
split_idx = lines.index('')

# process rules: |-separated string rule per line -> [(int, int), (int, int), ...]
rules = lines[:split_idx]
rules = [r.split('|') for r in rules]
rules = [(int(before), int(after)) for before, after in rules]

# process updates: comma-separated strings per line -> [[int, int,..], [int, ..], ...]
def split_and_cast(comma_separated_string):
    split = comma_separated_string.split(',')
    return [int(ea) for ea in split]

updates = lines[split_idx + 1:]
updates = [split_and_cast(update) for update in updates]

# test validity of each update; gather list of valid updates
valid = []

def is_valid(update, rule):
    lower, higher = rule
    if lower not in update or higher not in update:
        return True
    return update.index(lower) < update.index(higher)

for update in updates:
    valid_test = [is_valid(update, rule) for rule in rules]
    if all(valid_test):
        valid.append(update)

# sum middle page of valid updates
def get_middle(l):
    mid = len(l) // 2
    return l[mid]

print(sum(get_middle(valid_update) for valid_update in valid))