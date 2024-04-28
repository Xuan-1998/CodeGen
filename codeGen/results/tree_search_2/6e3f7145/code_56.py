def longest_palindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    max_length = 0
    center_index = 0

    for i in range(n):
        dp[i][i] = True

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j]:
                    max_length = length
                    center_index = i

    return s[center_index: center_index + max_length]
