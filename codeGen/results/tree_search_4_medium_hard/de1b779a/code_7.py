import sys

n, m, c0, d0 = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

def max_profit(i, j):
    if dp[i][j]:
        return dp[i][j]
    
    result = d0
    if i >= ci and ai >= bi:
        result = max(result, di - c0 + dp[i - ci][j - 1])
    
    dp[i][j] = result
    return result

for _ in range(m):
    ai, bi, ci, di = map(int, input().split())
    for i in range(n, ci - 1, -1):
        dp[i][m - _] = max(dp[i][m - _], di + max_profit(i - ci, m - _ - 1))
    for j in range(m - _, -1, -1):
        dp[n][j] = max(dp[n][j], d0)

print(max_profit(n, m))
