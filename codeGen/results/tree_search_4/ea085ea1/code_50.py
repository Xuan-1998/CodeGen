def max_common_substrings(str1, str2):
    N = len(str1)

    # Initialize dp and start arrays
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    start = [[0] * (N + 1) for _ in range(N + 1)]

    max_count = 0

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if str1[i - 1] == str2[j - 1]:
                if dp[i - 1][j - 1] > 0:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    start[i][j] = i if dp[i][j] == 1 else start[i - 1][j - 1]
                else:
                    dp[i][j] = 1
                    start[i][j] = i

            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    for i in range(N + 1):
        for j in range(N + 1):
            if dp[i][j] > max_count:
                max_count = dp[i][j]
                # Extract the actual substrings using start indices
                pass

    return max_count
