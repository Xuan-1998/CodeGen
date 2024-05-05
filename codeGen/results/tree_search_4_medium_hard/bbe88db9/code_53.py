def count_portals(n, portals):
    MOD = 10**9 + 7

    dp = [[0] * (n + 2) for _ in range(n + 1)]

    dp[0][1] = 1
    for i in range(1, n + 1):
        for j in range(i + 1, n + 2):
            if j == n + 1:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i - 1][portals[i - 1]] + 1) % MOD

    return dp[n][n + 1]

n = int(input())
portals = [int(x) for x in input().split()]
print(count_portals(n, portals))
