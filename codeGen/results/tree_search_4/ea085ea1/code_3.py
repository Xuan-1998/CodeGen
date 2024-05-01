def max_common_substrings(str1, str2):
    N = len(str1)
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    # Fill the bottom row first (dp[N-1][j]) for j = 0 to N-1
    for j in range(N + 1):
        if j == 0:
            dp[N - 1][j] = 0
        elif str1[N - 1] == str2[j - 1]:
            dp[N - 1][j] = 1 + dp[N - 1][j - 1]
        else:
            dp[N - 1][j] = max(dp[N - 1][j - 1], N)

    # Fill in each subsequent row
    for i in range(N - 2, -1, -1):
        for j in range(N + 1):
            if str1[i] == str2[j]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(min(dp[i - 1][j], dp[i][j - 1]), N)

    return dp[0][N - 1]

str1 = input()
str2 = input()

print(max_common_substrings(str1, str2))
