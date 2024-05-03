import sys

n, m = map(int, sys.stdin.readline().split())
plants = []
for _ in range(n):
    species, x = map(float, sys.stdin.readline().split())
    plants.append((int(species), float(x)))
plants.sort(key=lambda x: x[1])

dp = [[float('inf')] * (m + 1) for _ in range(n)]
prev_species = None
for i, (species, x) in enumerate(plants):
    for j in range(m):
        if species == j + 1:  # plant belongs to this section
            dp[i][j] = 0
        elif j > 0 and prev_species == j:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + 1
        else:
            dp[i][j] = float('inf')
    prev_species = species

min_replantings = float('inf')
for j in range(m):
    min_replantings = min(min_replantings, dp[-1][j])
print(min_replantings)
