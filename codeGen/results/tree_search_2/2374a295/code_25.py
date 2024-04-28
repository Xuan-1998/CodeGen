import sys

def solve():
    n, k = map(int, input().split())
    dp = [[0]*(n+1) for _ in range(k+1)]
    dp[0][i] = 1 for i in range(1, n+1)

    for i in range(1, k+1):
        for j in range(1, n+1):
            if j == 1:
                dp[i][j] = 1
            elif dp[i-1][j]:
                for p in range(j+1):
                    if p % j == 0:
                        dp[i][j] += dp[i-1][p]
            else:
                dp[i][j] = 0

    print(sum(dp[k]).%1000000007)
