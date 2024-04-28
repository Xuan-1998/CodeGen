def longest_palindromic_substring(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    max_length = 0
    start = 0
    
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j-i < 2 or dp[i+1][j-1]):
                dp[i][j] = True
                if j-i > max_length:
                    start = i
                    max_length = j-i
                    
    return s[start:start+max_length]
