def can_merge(p):
    n = len(p) // 2

    # dp table initialization
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        if p[i - 1] < p[n]:
            dp[0][i] = True
        else:
            dp[0][i] = False

    # fill up the dp table
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if p[i - 1] < p[j]:
                dp[i][j] = dp[0][j]
            elif p[i - 1] > p[j]:
                dp[i][j] = dp[i][0]

    return "YES" if any(dp[i][n]) else "NO"
