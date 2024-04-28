def max_non_overlapping_substrings(str1, str2):
    N = len(str1)
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # Check if characters at indices i and j match
            if str1[i - 1] == str2[j - 1]:
                # If they match, increment the count only if the substring doesn't overlap with previous ones
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j-1]) + (dp[i-1][j-1] > 0)
            else:
                # If they don't match, reset the count
                dp[i][j] = 0

    return dp[N][N]
