def cost(s):
    rev_count = 0
    for other in input_strings:
        if s > other:  # s is greater than the other string
            while s > other:
                s = s[::-1]
                rev_count += 1
        elif s < other:  # s is smaller than the other string
            pass  # no need to reverse s
    return rev_count

# Read input strings and costs from stdin
n = int(input())
input_strings = []
costs = []
for _ in range(n):
    cost, s = input().split()
    costs.append(int(cost))
    input_strings.append(s)

# Calculate the minimum total cost
min_cost = float('inf')
for i in range(2**n):
    rev_count = 0
    for j in range(n):
        if (i >> j) & 1:  # string j is reversed
            rev_count += costs[j]
    sorted_strings = [''] * n
    for j in range(n):
        if (i >> j) & 1:
            sorted_strings[j] = input_strings[j][::-1]
        else:
            sorted_strings[j] = input_strings[j]
    sorted_strings.sort()
    if sorted_strings == input_strings:
        min_cost = min(min_cost, rev_count)

# Print the minimum total cost to stdout
print(min_cost)
