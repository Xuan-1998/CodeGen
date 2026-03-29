from collections import defaultdict
import sys

# Read input
n = int(input())
M = list(map(int, input().split()))

# Initialize hashmap for indices of elements in M
index_map = defaultdict(list)

for i, m in enumerate(M):
    index_map[m].append(i)

# Calculate the number of ways to create V
ways = 1
prev_element_index = None
for element in sorted(M):
    if prev_element_index is not None:
        for idx in index_map[element]:
            # If an index is already used, it's a different way
            if M[idx] != element or prev_element_index != -1:
                ways *= 2
                break
    prev_element_index = idx

# Print the result modulo 10^9+7
print(ways % (10**9 + 7))
