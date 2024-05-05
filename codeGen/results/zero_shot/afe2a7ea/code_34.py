import sys

MOD = 998244353

def solve(n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][i] = 1
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length
            dp[i][j] = (dp[i][j-1] * (n - j + 1)) % MOD
    return dp[0][n]

n = int(sys.stdin.readline())
print(solve(n))
