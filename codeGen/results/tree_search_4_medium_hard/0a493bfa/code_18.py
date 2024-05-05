def beauty_array():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(m + 1):
            if j == 0:
                dp[i][j] = f(a[0])
            else:
                if j > 0 and a[i] % b[j] == 0:
                    dp[i][j] = max(dp[i - 1][k] for k in range(m + 1)) + a[i]
                else:
                    if i > 1:
                        dp[i][j] = max(dp[i - 1][k] for k in range(m + 1))
                    else:
                        dp[i][j] = f(a[0])

    return dp[n][m]
