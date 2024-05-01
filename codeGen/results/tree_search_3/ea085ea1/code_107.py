def max_common_substrings(str1, str2):
    N = len(str1)
    M = len(str2)

    # Initialize the 2D table with zeros
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    # Fill the table using a sliding window approach
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The maximum number of common non-overlapping substrings is stored in the bottom-right cell
    return dp[N][M]
