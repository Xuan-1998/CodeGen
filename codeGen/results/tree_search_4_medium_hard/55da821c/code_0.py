import sys
from collections import defaultdict

def greenhouse_plants():
    n, m = map(int, input().split())
    species_count = defaultdict(list)
    
    for _ in range(n):
        s, x = map(float, input().split())
        species_count[int(s)].append(x)

    dp = [[0] * (n + 1) for _ in range(m)]
    prev_section = 0

    for i in range(1, m):
        for j in range(len(species_count[i])):
            if species_count[i][j] <= x:
                break
            if dp[prev_section][j] < dp[i-1][j-1] + 1:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = dp[i-1][j]
        prev_section += 1

    return min(dp[-1])

print(greenhouse_plants())
