def longest_palindrome(s):
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]

    max_len = 0
    start_idx = 0

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                dp[i][j] = True
                if j - i > max_len:
                    max_len = j - i
                    start_idx = i

    return s[start_idx:start_idx + max_len]
