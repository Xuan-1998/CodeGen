import sys
from collections import defaultdict

def min_replantings(n, m):
    plants = [[] for _ in range(m+1)]
    for i in range(1, n+1):
        s, x = [int(x) for x in input().split()]
        plants[s].append((x, 0))  # (position, replanting count)

    dp = [[0] * m for _ in range(n+1)]
    for i in range(2, n+1):
        for j in range(m):
            if not plants[j]:
                continue
            prev_replantings = [x[1] for x in plants[j][:-1]]
            min_replanted = float('inf')
            for replanting in prev_replantings:
                dp[i][j] = min(dp[i-1][j], dp[i-1][replanting] + 1)
                if dp[i][j] < min_replanted:
                    min_replanted = dp[i][j]
            if i > 1 and j > 0:
                prev_species = plants[j-1][-1][0]
                dp[i][j] = min(dp[i][j], dp[i-1][prev_species] + 1)
    return min(dp[n])

n, m = [int(x) for x in input().split()]
print(min_replantings(n, m))
