def max_similarity_score():
    n, m = map(int, input().split())
    a = input()
    b = input()

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                k = dp[i - 1][j - 1] + 1
                dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])

    return 4 * (dp[n][m]) - (n + m)

print(max_similarity_score())
