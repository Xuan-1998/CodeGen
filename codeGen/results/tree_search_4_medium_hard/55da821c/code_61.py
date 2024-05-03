import sys
from collections import defaultdict

# Read input and initialize variables
n, m = map(int, input().split())
species_plants = defaultdict(list)
for _ in range(n):
    species, x = map(int, input().split())
    species_plants[species].append(x)

dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if species_plants[j][i - 1]:
            dp[i][j] = min((dp[i - 1].index(min(dp[i - 1])) or (n - 1)) + 1 if i == len(species_plants[j]) else dp[i - 1][j], dp[i][j])
        else:
            dp[i][j] = dp[i - 1][j]

print(min(dp[n]))
