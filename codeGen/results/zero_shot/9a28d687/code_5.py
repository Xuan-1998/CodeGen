# Step 1: Read the input
n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

# Step 2: Initialize the minimum total cost as infinity
min_cost = float('inf')

# Step 3: Iterate over all possible permutations of strings and calculate their cost
from itertools import permutations

for p in permutations(strings):
    total_cost = sum(costs[i] * (len(p) - i - 1) for i in range(len(p)))
    
    # Step 4: Check if the permutation is lexicographically sorted
    if all(p[i] <= p[i+1] for i in range(len(p)-1)):
        min_cost = min(min_cost, total_cost)

# Step 5: Print the minimum total cost required to sort the strings in lexicographical order
print(min_cost) if min_cost != float('inf') else print(-1)
