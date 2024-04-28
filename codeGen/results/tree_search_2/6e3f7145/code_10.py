def longest_palindromic_substring(s):
    if not s:
        return ""

    n = len(s)
    dp = [[False] * n for _ in range(n)]

    max_length = 0
    start_index = 0

    for i in range(n):
        dp[i][i] = True

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j]:
                if length == 2 or dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if length > max_length:
                        max_length = length
                        start_index = i
    return s[start_index:start_index + max_length]
