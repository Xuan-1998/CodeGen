def max_common_substrings(str1, str2):
    N = len(str1)
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for k in range(1, min(i + 1, N + 1)):
            if str1[i - k:i].endswith(str2[:k]):
                dp[i][k] = max(dp[i - 1][k - 1], dp[i][k])
            else:
                dp[i][k] = dp[i - 1][k]

    return max(dp[N - 1])

str1, str2 = input().split()
print(max_common_substrings(str1, str2))
