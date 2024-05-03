import sys
from collections import defaultdict

def min_replanting_plants():
    n, m = map(int, input().split())
    plants = list(map(lambda x: int(x), input().split()))
    species_counts = defaultdict(int)

    for plant in plants:
        species_counts[plant] += 1

    dp = [[0] * (m + 1) for _ in range(m + 1)]
    prev_species = -1
    prev_plants = 0

    for i in range(1, m + 1):
        for j in range(i):
            if plants[j-1] != i:
                prev_species = i
                prev_plants = sum(count for k, count in species_counts.items() if k == prev_species)
            dp[i][j] = min(dp[i][j-1], prev_plants + (sum(count for k, count in species_counts.items() if k != prev_species) if prev_species != -1 else 0))

    return dp[m][m]

print(min_replanting_plants())
