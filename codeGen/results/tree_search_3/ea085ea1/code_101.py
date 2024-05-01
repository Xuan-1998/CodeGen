def common_substrings(str1, str2):
    N = len(str1)
    M = len(str2)

    dp = [[0] * (M + 1) for _ in range(N + 1)]

    max_length = 0
    count = 0

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    count += 1
            else:
                dp[i][j] = 0

    return count
