import sys

def min_replant(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    res = [float('inf')] * (m + 1)

    for i in range(1, n + 1):
        s_i = int(input())
        if i > 0:
            for j in range(1, m + 1):
                if s_i == j:
                    dp[i][j] = dp[i-1][s_i]
                else:
                    dp[i][j] = min(dp[i-1][k] + 1 for k in range(1, m+1)) or dp[i-1][j]
        res[s_i] = min(res[s_i], dp[i][s_i])

    return min(res[1:])

n, m = map(int, input().split())
print(min_replant(n, m))
