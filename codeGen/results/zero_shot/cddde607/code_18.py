import sys
from collections import deque

k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def solve():
    dp = [[[0] * (k+1) for _ in range(n)] for _ in range(n)]
    dp[0][0][0] = 1
    for i in range(1, n):
        for j in range(i+1):
            if arr[i][j] <= k:
                dp[i][j][arr[i][j]] += dp[i-1][j][arr[i-1][j]]
                if j > 0:
                    dp[i][j][arr[i][j]] += dp[i-1][j-1][arr[i-1][j-1]]
    return dp[-1][-1][k]

print(solve())
