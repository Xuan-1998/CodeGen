import sys
from collections import defaultdict

# Read input from stdin
n, m = map(int, input().split())
plants = []
for _ in range(n):
    s, x = map(float, input().split())
    plants.append((int(s), x))

# Sort the plants by their positions
plants.sort(key=lambda x: x[1])

# Initialize a 2D table to store the minimum number of replantings required for each species up to the ith plant
dp = [[0] * m for _ in range(n)]
species_count = defaultdict(int)

# Fill up the dp table in a bottom-up manner
for i, (s, x) in enumerate(plants):
    # Calculate the minimum number of replantings required for this plant
    species_count[s] += 1
    min_replanted = float('inf')
    for j in range(m):
        if s == j + 1:
            break
        min_replanted = min(min_replanted, dp[i-1][j])
    # Update the dp table and the minimum number of replantings required for this plant
    dp[i][s-1] = species_count[s]
    if i > 0:
        dp[i][s-1] += dp[i-1][s-1]
    min_replanted -= (species_count[s] - 1)
    dp[i][s-1] = min(dp[i][s-1], min_replanted)

# Print the minimum number of plants that need to be replanted
print(min(dp[-1]))

