def solve():
    n = int(input())
    MOD = 998244353
    dp = [[0] * (n + 1) for _ in range(n + 2)]
    for i in range(n + 1):
        dp[0][i] = 1 if i == 0 else 0
    for i in range(1, n + 1):
        for j in range(i + 1):
            if j >= 1:
                for k in range(j + 1):
                    dp[i][j] = (dp[i][j] or ((k != 0) and (i % 2 != 0)) and (min(j - 1, i - 1) < k) and dp[i - k][min(j - 1, k - 1)])
    print(dp[n][n])
