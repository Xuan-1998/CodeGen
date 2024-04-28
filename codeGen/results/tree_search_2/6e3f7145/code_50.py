def longest_palindrome(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    max_len = 0
    center = -1

    for i in range(n):
        for j in range(i, n):
            if s[i] == s[j]:
                if i == j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    center = i

    return s[center:center + max_len]

