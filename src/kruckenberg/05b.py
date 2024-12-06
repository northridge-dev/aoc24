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

# test invalidity of each update; gather list of invalid updates
def is_invalid(update, rule):
    lower, higher = rule
    return lower in update and higher in update and update.index(lower) > update.index(higher)

def find_invalid_updates(updates, rules, test_fn):
    invalid = []
    for update in updates:
        test_results = [test_fn(update, rule) for rule in rules]
        if any(test_results):
            invalid.append(update)

    return invalid

invalid = find_invalid_updates(updates, rules, is_invalid)

# fix invalid updates
def fix_order(update, rules, test_fn):
    fixed = update.copy()
    for rule in rules:
        if test_fn(fixed, rule):
            lower, higher = rule
            fixed.remove(lower)
            fixed.insert(fixed.index(higher), lower)
    return fixed

fixed = []

for update in invalid:
    nupdates = 0
    reordered = update.copy()
    while find_invalid_updates([reordered], rules, is_invalid) and nupdates < 3:
        reordered = fix_order(reordered, rules, is_invalid)
        nupdates += 1    
    fixed.append(reordered)

# sum middle page of fixed updates
def get_middle(l):
    mid = len(l) // 2
    return l[mid]

print(sum(get_middle(fixed_update) for fixed_update in fixed))