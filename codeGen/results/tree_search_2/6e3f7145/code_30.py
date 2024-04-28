def longest_palindrome(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    max_length = 0
    center_index = 0

    for i in range(n):
        for j in range(i, -1, -1):
            if s[i] == s[j]:
                if i - j < 2:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j+1]
                if i - j > max_length:
                    max_length = i - j
                    center_index = (i + j) // 2

    return s[center_index - max_length: center_index + max_length]

s = input()
print(longest_palindrome(s))
