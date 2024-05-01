def max_common_substrings(str1, str2):
    N = len(str1)
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(N - 1, -1, -1):
        for k in range(1, min(i + 2, N + 1)):
            if str1[i - k + 1:i + 1] == str2[i - k + 1:i + 1]:
                dp[i][k] = dp[i - 1][k - 1] + 1
            else:
                dp[i][k] = max(dp[j][l] for j in range(i) for l in range(1, k + 1))

    return dp[-1][-1]
