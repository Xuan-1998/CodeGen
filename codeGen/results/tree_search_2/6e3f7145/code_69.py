def longest_palindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    max_length = 0
    center_index = 0

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j]:
                if j - i < 2 or dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if j - i > max_length:
                        max_length = j - i
                        center_index = (i + j) // 2

    return s[center_index - max_length // 2: center_index + max_length // 2 + 1]

s = input()
print(longest_palindrome(s))
