def longest_palindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    max_length = 0
    start = 0
    
    for i in range(n):
        for j in range(i+1):
            if s[j] == s[i]:
                if j == i or dp[j-1][i-1]:
                    dp[j][i] = True
                    if i - j + 1 > max_length:
                        max_length = i - j + 1
                        start = j
    
    return s[start:start+max_length]
