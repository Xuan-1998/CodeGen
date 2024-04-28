def longest_palindromic_substring(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for length in range(2, n+1):
        for i in range(n-length):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])

    max_length = 0
    for i in range(n):
        for j in range(i, n):
            if dp[i][j] > max_length:
                max_length = dp[i][j]
                start_idx = i

    return s[start_idx:start_idx+max_length]
