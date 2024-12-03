import re


with open('day3_input.txt') as f:
    data = f.readlines()
    data = "".join(data)

# match = re.findall(r'(mul\((\d{1,3}),(\d{1,3})\))', data)
# print(match)
#
# acc = 0
#
# for cap in match:
#     acc += int(cap[1]) * int(cap[2])
#
# print(acc)

# ------------------- PART 2 -------------------
match = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))", data)
print(match)

do = True
acc = 0
for cap in match:
    if cap[2] == "do()":
        do = True
    elif cap[3] == "don't()":
        do = False
    else:
        if do:
            acc += int(cap[0]) * int(cap[1])


print(acc)