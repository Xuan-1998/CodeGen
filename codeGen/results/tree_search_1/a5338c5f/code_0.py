import sys
from collections import defaultdict

# Read input from stdin
n, s, k = map(int, input().split())
ri = list(map(int, input().split()))
ci = input().strip()

# Initialize the dynamic programming table
# We use defaultdict to handle cases where a state has not been visited
dp = defaultdict(lambda: float('inf'))
dp[(s - 1, 0, 'N')] = 0  # N represents no color as the starting point

# Iterate through each box
for i in range(n):
    # Iterate through all possible numbers of candies eaten so far
    for j in range(k + 1):
        # Consider all three colors
        for c in 'RGBN':  # N represents the start where no color is eaten
            # If this state is not possible, skip it
            if dp[(i, j, c)] == float('inf'):
                continue
            # Eat candies from the current box if the color is different
            if ci[i] != c and j + ri[i] <= k:
                dp[(i, j + ri[i], ci[i])] = min(dp[(i, j + ri[i], ci[i])], dp[(i, j, c)])
            # Move to the next box if there are more candies and update the time
            if i + 1 < n and ri[i + 1] > ri[i]:
                dp[(i + 1, j, c)] = min(dp[(i + 1, j, c)], dp[(i, j, c)] + 1)
            # Move to the previous box if there are more candies and update the time
            if i - 1 >= 0 and ri[i - 1] > ri[i]:
                dp[(i - 1, j, c)] = min(dp[(i - 1, j, c)], dp[(i, j, c)] + 1)

# Find the minimum time to eat at least k candies
min_time = float('inf')
for i in range(n):
    for c in 'RGB':
        min_time = min(min_time, dp[(i, k, c)])

# Print the result
if min_time == float('inf'):
    print(-1)
else:
    print(min_time)
