def smallest_string(n, k):
    s = input()
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = s[:i]

    for j in range(1, k + 1):
        for i in range(j - 1, n + 1):
            if i < n and s[i] == s[j-1]:
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1] + s[i-1], dp[i-1][j])

    return dp[n][k]

n, k = map(int, input().split())
print(smallest_string(n, k))
