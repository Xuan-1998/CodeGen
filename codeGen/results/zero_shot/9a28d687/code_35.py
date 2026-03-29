code block:
# read input
n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

# initialize variables
total_cost = 0
sorted_strings = []

# sort the strings
for i in range(n):
    # find the string that is closest to being sorted
    min_diff = float('inf')
    min_str = None
    for j in range(n):
        diff = abs(len(strings[j]) - len(sorted_strings[-1]))
        if diff < min_diff:
            min_diff = diff
            min_str = strings[j]
    
    # reverse the string and add it to the sorted list
    total_cost += costs[sorted_strings.index(min_str)]
    sorted_strings.append(min_str[::-1])
