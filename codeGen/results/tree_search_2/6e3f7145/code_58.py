def longest_palindrome(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1  # single characters are palindromes

    max_length = 0
    start = 0

    for i in range(n):
        for j in range(i, n):
            if s[i] == s[j]:  # check if the characters match
                if j - i + 1 < 3:  # single or double characters are palindromes
                    dp[i][j] = 1
                elif dp[i+1][j-1]:  # check if the substring without these characters is a palindrome
                    dp[i][j] = 1
            if dp[i][j] and j - i + 1 > max_length:
                max_length = j - i + 1
                start = i

    return s[start:start+max_length]
