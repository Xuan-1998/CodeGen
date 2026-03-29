def smallest_string(n, k):
    s = input().strip()
    dp = [[s[:i+1]] + [None] * (k-i) for i in range(k+1)]

    for i in range(1, n+1):
        for j in range(min(i, k), -1, -1):
            if j >= k:
                dp[i][j] = s[:k]
            elif len(s) > 0 and (len(s)-1 < j or dp[i-1][j-1][0] <= s[-1]):
                dp[i][j] = dp[i-1][j-1][0]
            else:
                dp[i][j] = s[:i+1]

    return dp[n][k-1].strip()
