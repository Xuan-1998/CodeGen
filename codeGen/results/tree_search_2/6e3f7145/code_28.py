def longest_palindromic_substring(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    max_length = 1
    center = 0
    
    for i in range(n):
        dp[i][i] = True
        
    for start in range(n-1, -1, -1):
        for end in range(start, n):
            if s[start] == s[end]:
                if end-start < 2:
                    dp[start][end] = True
                    max_length = 1
                    center = start
                else:
                    dp[start][end] = dp[start+1][end-1]
            else:
                dp[start][end] = False
    
    return s[center-center//max_length: center + max_length]
