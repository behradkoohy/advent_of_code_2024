import heapq

with open('day1_input.txt') as f:
    data = f.readlines()
    data = [d.replace('\n', '') for d in data]
    data = [d.split('   ') for d in data]



left = [int(d[0]) for d in data]
right = [int(d[1]) for d in data]

left_heap = heapq.heapify(left)
right_heap = heapq.heapify(right)

total_difference = 0
for _ in range(len(left)):
    total_difference += abs(heapq.heappop(left) - heapq.heappop(right))

print(total_difference)