from math import inf
MOD = 10**9 + 7

def solve(n):
    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][i] = 1
    for len_ in range(2, n+1):
        for i in range(1, n+1 - len_ + 1):
            j = i + len_ - 1
            for k in range(i-1, j):
                if M[k] < M[i]:
                    dp[i][j] += dp[i-1][k]
            dp[i][j] %= MOD
    return dp[1][n]

M = [int(x) for x in input().split()]
print(solve(len(M)))
