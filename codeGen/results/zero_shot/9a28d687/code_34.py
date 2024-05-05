# Step 1: Read the input
n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

# Step 2: Create a priority queue to store the strings along with their costs and indices
from heapq import heapify, heappop, heappush
pq = [(c, i, s) for i, (c, s) in enumerate(zip(costs, strings))]
heapify(pq)

# Step 3: Initialize variables to keep track of the sorted string and its cost
min_cost = 0
sorted_strings = []

# Step 4: Sort the strings by repeatedly popping the smallest-cost string from the priority queue, reversing it if necessary, and adding it to the sorted list
while pq:
    _, i, s = heappop(pq)
    if not sorted_strings or s < sorted_strings[-1]:
        min_cost += costs[i]
        sorted_strings.append(s)
    else:
        min_cost += 2 * costs[i]
        sorted_strings.append(s[::-1])

# Step 5: Check if the strings are sorted in lexicographical order. If not, print -1.
if ''.join(sorted_strings) != sorted(''.join(sorted_strings)):
    print(-1)
else:
    print(min_cost)
