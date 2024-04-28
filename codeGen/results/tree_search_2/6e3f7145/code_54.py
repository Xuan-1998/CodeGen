import sys

def longest_palindromic_substring(s):
    n = len(s)
    dp = [False] * (n + 1)

    for i in range(n + 1):
        dp[i] = True

    for i in range(1, n + 1):
        for j in range(i):
            if s[j] == s[i - 1]:
                if i % 2 == 1:
                    dp[i] = True
                elif dp[(i - 1) // 2]:
                    dp[i] = True

    max_length = 0
    result = ""
    for i in range(n + 1):
        if dp[i] and i > max_length:
            max_length = i
            result = s[:i]

    return result

s = input()
print(longest_palindromic_substring(s))
