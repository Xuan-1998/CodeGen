def longest_palindromic_substring(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    max_len = 0
    res = ""
    
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j-i < 2 or dp[i+1][j-1]):
                dp[i][j] = True
                if j-i+1 > max_len:
                    max_len = j-i+1
                    res = s[i:j+1]
    
    return res
