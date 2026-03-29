def solve(n, p):
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(min(i, n), -1, -1):
            if p[j-1] > p[j]:
                dp[i][j] = (dp[i-1][k] for k in range(j) if p[k] < p[j-1]) | {True}
            elif p[j-1] < p[j]:
                dp[i][j] = (dp[i-1][k] for k in range(j+1, n) if p[k] > p[j-1]) | {False}

    return "YES" if dp[n][n] else "NO"
