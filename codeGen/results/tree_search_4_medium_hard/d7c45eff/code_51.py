def smallest_string(n, k):
    s = input().strip()
    dp = [[['' for _ in range(k+1)] for _ in range(n+1)] for _ in range(2)]

    for i in range(n+1):
        dp[0][i][0] = ''
        if i > 0:
            dp[0][i][0] = s[:i]

    for j in range(k+1):
        dp[1][n][j] = s * (k // len(s) + 1)
        if k % len(s) != 0 and j < k % len(s):
            dp[1][n][j] += s

    for i in range(1, n+1):
        for j in range(min(i, k)+1):
            if len(s[:i]) <= j:
                dp[1][i][j] = min(dp[0][i-1][j], dp[1][i-1][j-1] + s[i-1])
            else:
                dp[1][i][j] = dp[1][i-1][j]

    return dp[1][n][k].ljust(k, 'a') if k % len(s) != 0 else dp[1][n][k]
