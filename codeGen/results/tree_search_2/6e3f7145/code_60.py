def longest_palindrome(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    max_length = 0
    start_index = 0
    
    for i in range(n):
        dp[i][i] = 1
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = 1
                elif dp[i + 1][j - 1]:
                    dp[i][j] = 1
                
                if dp[i][j] and length > max_length:
                    max_length = length
                    start_index = i
    
    return s[start_index:start_index + max_length]
