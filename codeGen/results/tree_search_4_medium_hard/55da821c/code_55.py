import sys
from collections import defaultdict

def min_replantings():
    n, m = map(int, input().split())
    plants = [list(map(int, input().split())) for _ in range(n)]
    plants.sort(key=lambda x: x[1])

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    species_count_map = defaultdict(int)

    for i in range(1, n + 1):
        species_count_map[plants[i-1][0]] += 1

        for j in range(m, 0, -1):
            if plants[i-1][0] == j:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + species_count_map[j]
                break
            elif j > 1 and plants[i-1][0] < j:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + (species_count_map[j] - species_count_map.get(j-1, 0) if j > 1 else 0)
            else:
                dp[i][j] = dp[i-1][j]

    print(dp[n][m])

min_replantings()
