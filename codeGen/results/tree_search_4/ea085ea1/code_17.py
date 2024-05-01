def max_common_substrings(str1, str2):
    N = len(str1)
    dp = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(min(i, j), 0, -1):
                if str1[i - k:i] == str2[j - k:j]:
                    dp[i][j][k] = max(dp[i - 1][j - 1][k - 1], dp[i - 1][j][k]) + 1
    return dp[N][N][N]
