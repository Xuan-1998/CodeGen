import sys

def solve():
    t = int(input())
    MOD = 10**8 + 7
    dp = [[0] * (m+1) for _ in range(n+1)]

    # Base case: empty string
    dp[0][0] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if 2*i <= n:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][m-j]) % MOD
            else:
                dp[i][j] = dp[i-1][m-j-1]
        for j in range(1, m+1):
            if 2*i > n:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][m-j]) % MOD
            else:
                dp[i][j] = dp[i-1][m-j-1]

    for _ in range(t):
        n, m = map(int, input().split())
        print((dp[n][m] + 1) % MOD)

solve()
