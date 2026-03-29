import heapq
n = int(input())
costs_and_strings = []
for _ in range(n):
    cost, string = input().split()
    costs_and_strings.append((int(cost), len(string), 0, string))

sorted_costs_and_strings = sorted(costs_and_strings)

total_cost = 0
last_string_length = 0

heap = []

for cost, length, _, string in sorted_costs_and_strings:
    if last_string_length > 0 and length < last_string_length:
        # Reverse the string to make it smaller than the previous one
        total_cost += cost
    while heap and heap[0][1] < length:
        heapq.heappop(heap)
    for _ in range(len(heap)):
        _, heap_size = heapq.heappop(heap)
        total_cost -= heap_size * cost
    heap.extend([(length, 1)] * (last_string_length - length))
    last_string_length = length

print(total_cost) if not heap else print(-1)
