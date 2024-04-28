import sys

# Read input
n = int(input())
garland = input()

# Initialize dp array with maximum possible value (for now)
dp = [sys.maxsize] * (n + 1)

# Base case: no recolors needed for an empty garland
dp[0] = 0

# Fill dp array using dynamic programming
for i in range(1, n + 1):
    prev_colors = garland[i - 3:i]
    if len(set(prev_colors)) == 2:  # If the last three colors are distinct
        dp[i] = min(dp[i], 1 + (dp[i - 1] if i > 0 else 0))
    else:
        dp[i] = min(dp[i], dp[i - 1])

# Find the minimum number of recolors needed and construct a diverse garland
r = dp[-1]
garland_diverse = ''
colors_used = set()
for i in range(n):
    if (i % 3 == 0 and 'R' not in colors_used) or \
       (i % 3 == 1 and 'G' not in colors_used) or \
       (i % 3 == 2 and 'B' not in colors_used):
        garland_diverse += 'R' if len(colors_used) < 2 else ('G' if 'R' not in colors_used else 'B')
    else:
        garland_diverse += garland[i]
    if i < n - 1:
        colors_used.add(garland_diverse[-1])

print(r)
print( garland_diverse )
