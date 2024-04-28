import sys

def longest_palindrome(s):
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    max_len = 0
    start = 0

    for i in range(1, n + 1):
        for j in range(i, -1, -1):
            if s[j] == s[i-1]:
                dp[j][i] = (dp[(j+1)][(i-1)] or not s[j+1:i].lstrip(s[j]).count(s[j]) > 0)
                if dp[j][i] and i - j > max_len:
                    max_len = i - j
                    start = j

    return s[start:start + max_len]

s = input()
print(longest_palindrome(s))
