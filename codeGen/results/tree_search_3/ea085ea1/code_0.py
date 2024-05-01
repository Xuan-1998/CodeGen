def max_common_substrings(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    max_len = 0
    for i in range(m, -1, -1):
        for j in range(n, -1, -1):
            if str1[i] == str2[j]:
                max_len = max(max_len, dp[i][j])
                while max_len > 0 and (i - max_len < 0 or j - max_len < 0 or str1[i - max_len] != str2[j - max_len]):
                    max_len -= 1

    return max_len
