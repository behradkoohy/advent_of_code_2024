
with open('day2_input.txt') as f:
    data = f.readlines()
    data = [d.replace('\n', '') for d in data]
    data = [d.split(' ') for d in data]
    data = [[int(d) for d in ds] for ds in data]

safe_count = 0

def non_decreasing(L):
    return all(x<=y for x, y in zip(L, L[1:]))

def non_increasing(L):
    return all(x>=y for x, y in zip(L, L[1:]))

def is_safe(row):
    l = 1
    while l < len(row):
        if 1 <= abs(row[l - 1] - row[l]) <= 3:
            l += 1
        else:
            return False
    if non_decreasing(row) or non_increasing(row):
        return True
    else:
        return False

# print(is_safe([1,3,6,7,9]))
for row in data:
    if is_safe(row):
        safe_count += 1
    else:
        sub_l = 0
        lists_to_check = []

        while sub_l < len(row):
            lists_to_check.append(row[:sub_l] + row[sub_l + 1:])
            sub_l += 1
        print(lists_to_check)
        for l in lists_to_check:
            if is_safe(l):
                safe_count += 1
                break



print(safe_count)

# ------------------- PART 2 -------------------

