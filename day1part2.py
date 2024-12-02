with open('day1_input.txt') as f:
    data = f.readlines()
    data = [d.replace('\n', '') for d in data]
    data = [d.split('   ') for d in data]



left = [int(d[0]) for d in data]
right = [int(d[1]) for d in data]

left_count = {}
right_count = {}

for l, r in zip(left, right):
    left_count[l] = left_count.get(l, 0) + 1
    right_count[r] = right_count.get(r, 0) + 1

print(right_count)

total_similarity = 0
for l, r in zip(left, right):
    total_similarity = total_similarity + (l * right_count.get(l, 0))
    # total_similarity = total_similarity + (r * left_count[l])

print(total_similarity)