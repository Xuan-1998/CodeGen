import sys
from collections import defaultdict

def min_replanted():
    n, m = map(int, input().split())
    plants = [[s, x] for s, x in (map(int, line.split()) for line in sys.stdin.readlines()[:-1])]
    plants.sort(key=lambda x: x[1])

    dp = [[[float('inf')] for _ in range(n+1)] for _ in range(m+1)]
    dp[0][0] = 0

    for i in range(1, m+1):
        for j in range(i, n+1):
            for k in range(i-1, -1, -1):
                if plants[j-1][0] == k:
                    break
            dp[i][j] = min(dp[i][j], dp[k][j-k]+1)

    return dp[m][n]

print(min_replanted())
