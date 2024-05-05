import sys

# Read the input
n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

# Sort the strings based on their lengths and then themselves
sorted_strings = sorted((len(s), s) for s in strings)

# Initialize the minimum cost and the last string seen
min_cost = 0
last_seen = ""

# Iterate over the sorted strings and calculate the minimum cost
for _, s in sorted_strings:
    if s != last_seen:
        min_cost += costs[sorted_strings.index((len(s), s))]
    last_seen = s

# Print the result
print(min_cost)
