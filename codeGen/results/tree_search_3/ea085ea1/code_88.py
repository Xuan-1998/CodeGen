def max_common_substrings(str1, str2):
    N = len(str1)
    dp = [[[0] * (N+1) for _ in range(N+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, N+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j][0] = max(dp[i-1][j-1][0], 1) + (dp[i-1][j-1][0] or 0)
            else:
                dp[i][j][0] = 0

    max_length = 0
    for i in range(N+1):
        for j in range(N+1):
            if dp[i][j][0] > max_length:
                max_length = dp[i][j][0]

    return max_length

str1 = input()
str2 = input()

print(max_common_substrings(str1, str2))
