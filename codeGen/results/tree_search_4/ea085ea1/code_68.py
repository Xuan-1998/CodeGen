def max_common_substrings(str1, str2):
    N = len(str1)
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])

    return dp[N][N]

# Receive input from stdin
str1, str2 = [line.strip() for line in sys.stdin.readlines()]

# Calculate the maximum number of common non-overlapping substrings
max_count = max_common_substrings(str1, str2)

print(max_count)
