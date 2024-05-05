def solve():
    n = int(input())
    MOD = 998244353
    dp = [[0] * (n + 2) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(i, n + 2):
            if f(i, j):  # function f not implemented yet
                for k in range(j - 1, -1, -1):
                    dp[i][j] = (dp[i][j] + dp[k][j - 1]) % MOD

    return dp[n][n]

def f(i, j):
    # implement this function later
    pass

print(solve())
