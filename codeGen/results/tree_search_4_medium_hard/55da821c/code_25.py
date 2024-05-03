import sys
from collections import defaultdict

# Read input
n, m = map(int, input().split())
plants = []
for _ in range(n):
    s, x = map(float, input().split())
    plants.append((int(s), x))

# Initialize DP array
dp = [[0] * (m + 1) for _ in range(n + 1)]
sections = defaultdict(list)

# Preprocess the plants by sorting them and grouping them by species
plants.sort(key=lambda x: x[1])
for s, x in plants:
    sections[s].append((s, x))

# Fill up the DP array
for i in range(1, n + 1):
    for j in range(min(i + 1, m) + 1):  # Only consider valid section indices
        min_replanted = sys.maxsize
        for last_species, last_x in sections[j - 1]:
            if x > last_x:  # The current plant should be placed after the last plant of this species
                replanted = dp[i - 1][j] + (last_species != j)
                min_replanted = min(min_replanted, replanted)
        for s, x in sections[j]:
            if x > plants[i - 1][1]:  # The current plant should be placed after the last plant of this species
                replanted = dp[i - 1][j] + (s != j)
                min_replanted = min(min_replanted, replanted)
        dp[i][j] = min_replanted

# Print the minimum number of plants that need to be replanted
print(dp[-1][-1])
