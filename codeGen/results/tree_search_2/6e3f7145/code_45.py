def longest_palindromic_substring(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # Fill the diagonal elements (single-character substrings)
    for i in range(n):
        dp[i][i] = 1

    # Fill the rest of the table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] or 1
            else:
                dp[i][j] = 0

    # Find the longest palindromic substring
    max_length = 0
    max_substring = ""
    for i in range(n):
        for j in range(i, n):
            if dp[i][j]:
                length = j - i + 1
                if length > max_length:
                    max_length = length
                    max_substring = s[i:j+1]

    return max_substring
