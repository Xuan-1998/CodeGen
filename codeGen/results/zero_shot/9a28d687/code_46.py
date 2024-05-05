python
import sys
from collections import defaultdict

n = int(sys.stdin.readline().strip())

costs = [0] * n
strings = [''] * n

for i in range(n):
    costs[i], string = sys.stdin.readline().strip().split()
    costs[i] = int(costs[i])
    strings[i] = string

# Step 1: Create a suffix array for each string
suffixes = []
for s in strings:
    suffixes.append(s)
    suffixes.append(s[::-1])  # Reverse the string

# Step 2: Sort the suffixes based on their lexicographical order
sorted_suffixes = sorted(suffixes)

# Step 3: Initialize a variable to store the minimum total cost
min_cost = 0

# Step 4: Iterate over the sorted suffixes and calculate the minimum total cost
for i in range(len(sorted_suffixes)):
    if len(sorted_suffixes[i]) % 2 == 1:
        min_cost += costs[sorted_suffixes.index(strings[i])]
    else:
        min_cost += costs[sorted_suffixes.index(strings[i]) + 1]

print(min_cost)
