def max_common_non_overlapping_substrings(str1, str2):
    N = len(str1)
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for k in range(1, N + 1):
        last_common_index = -1
        for i in range(k, N + 1):
            if str1[i-k:i+1] in str2:
                dp[i][k] = max(dp[i-1][k-1] + 1, dp[i-1][k])
                last_common_index = i
            else:
                dp[i][k] = dp[i-1][k]

    return dp[N][N]
