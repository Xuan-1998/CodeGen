import sys

def solve(n, m):
    MOD = 10**9 + 7
    dp = [[0] * (m+1) for _ in range(11)]

    for j in range(m+1):
        dp[0][j] = 1

    for i in range(1, 11):
        for j in range(i, -1, -1):
            if j == 0:
                dp[i][j] = 1
            else:
                for k in range(j+1):
                    dp[i][j] = min(dp[i][j], 1 + dp[k][j-1]) % MOD

    return dp[n][m]

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(solve(n, m))
