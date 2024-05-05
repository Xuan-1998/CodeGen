python
# Step 1: Read input
n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

# Step 2: Sort strings based on their lexicographical order
sorted_strings = sorted(strings)

# Step 3: Initialize minimum cost and total cost
min_cost = float('inf')
total_cost = 0

# Step 4: Iterate over the sorted strings to find the minimum cost
for i in range(n):
    if strings[i] != sorted_strings[i]:
        min_cost = min(min_cost, costs[i])
        total_cost += min_cost
    else:
        total_cost += costs[i]

print(total_cost)
