def longest_palindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    max_len = 0
    start_idx = 0

    for i in range(n):
        for j in range(i, -1, -1):
            if s[i] == s[j]:
                if j + 1 == i or not dp[j + 1][i - 1]:
                    dp[j][i] = True
                    if i - j > max_len:
                        max_len = i - j
                        start_idx = j

    return s[start_idx:start_idx + max_len]
