def max_common_substrings(str1, str2):
    N = len(str1)
    M = len(str2)

    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j] + dp[i][j - 1])
            else:
                dp[i][j] = 0

    return max(max(row) for row in dp)

# Test the function
str1 = input()
str2 = input()

print(max_common_substrings(str1, str2))
