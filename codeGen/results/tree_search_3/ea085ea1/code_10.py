def max_common_substrings(str1, str2):
    N = len(str1)
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[0][0]

str1, str2 = input().split()
print(max_common_substrings(str1, str2))
