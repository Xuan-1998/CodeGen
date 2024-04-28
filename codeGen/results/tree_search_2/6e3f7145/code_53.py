def longest_palindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    max_length = 0
    max_palindrome = ""

    for i in range(n):
        dp[i][i] = True

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = True
                elif dp[i + 1][j - 1]:
                    dp[i][j] = True

            if dp[i][j]:
                if length > max_length:
                    max_length = length
                    max_palindrome = s[i:j + 1]

    return max_palindrome
