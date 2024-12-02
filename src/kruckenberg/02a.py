from utils.files import readlines

reports_raw = readlines('02.txt');
reports = []

for report in reports_raw:
    split = report.split()
    cast_to_int = list(map(int, split))
    reports.append(cast_to_int)

def is_increasing(currVal, nextVal): return currVal < nextVal

def is_safe(report):
    increasing = is_increasing(report[0], report[1])

    for i in range(len(report) - 1):
        currVal, nextVal = report[i], report[i+1]
        if increasing != is_increasing(currVal, nextVal) or currVal == nextVal:
            return False
        if abs(currVal - nextVal) > 3:
            return False
    
    return True

num_safe = sum(1 for result in map(is_safe, reports) if result)
print(num_safe)