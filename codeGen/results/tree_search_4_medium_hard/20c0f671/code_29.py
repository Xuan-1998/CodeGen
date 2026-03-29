import sys

# Read input from stdin
n, shelf_width = map(int, input().split())
thicknesses, heights = [], []
for _ in range(n):
    t, h = map(int, input().split())
    thicknesses.append(t)
    heights.append(h)

# Initialize dp table with maximum possible height for each book on its own
dp = [[h] for h in heights]

# Fill up the dp table using bottom-up dynamic programming approach
for i in range(1, n):
    for j in range(shelf_width + 1):
        if thicknesses[i-1] <= j:
            dp[i].append(min(dp[i-1][j], dp[i-1][j-thicknesses[i-1]] + heights[i]))
        else:
            dp[i].append(dp[i-1][j])

# Print the minimum possible height of the bookcase
print(min(dp[-1]))

