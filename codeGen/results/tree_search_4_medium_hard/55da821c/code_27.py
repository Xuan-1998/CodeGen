import sys

def min_replanting(n, m):
    dp = [[float('inf')] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(min(i, m), -1, -1):  # Start from the end of the sections
            if i == j:
                dp[i][j] = 0
            else:
                for k in range(j-1, max(0, j-m), -1):  # Try all possible placements
                    dp[i][j] = min(dp[i][j], dp[k][j-1] + abs(i-k))

    return dp[n][m]

n, m = map(int, input().split())
print(min_replanting(n, m))
