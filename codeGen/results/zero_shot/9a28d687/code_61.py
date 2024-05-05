# Read input
n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

# Sort the strings based on their lengths
strings.sort(key=len)

# Initialize minimum cost and the current string index
min_cost = 0
curr_idx = 0

# Iterate through the sorted strings
for i in range(len(strings)):
    # If the current string is lexicographically smaller than the previous one, update the current index
    while curr_idx < n and (strings[i] < strings[curr_idx] or strings[i].endswith(strings[curr_idx])):
        min_cost += costs[curr_idx]
        curr_idx += 1

# If the last string is not reached, it's impossible to sort them in lexicographical order
if curr_idx < n:
    print(-1)
else:
    # Add the cost of reversing the last string
    min_cost += costs[-1]
    print(min_cost)
