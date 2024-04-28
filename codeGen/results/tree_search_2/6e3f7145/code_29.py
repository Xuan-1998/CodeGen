import sys

def longest_palindromic_substring(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    max_length = 0
    for i in range(n):
        dp[i][i] = True
    
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = (length == 1) or dp[i+1][j-1]
                if dp[i][j] and length > max_length:
                    max_length = length
    
    return s[max_length-1:max_length]

s = input()
print(longest_palindromic_substring(s))
