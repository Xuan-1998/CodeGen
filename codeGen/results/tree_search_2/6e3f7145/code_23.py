def longest_palindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    max_len = 0
    result = ""
    
    for i in range(n):
        for j in range(i, n):
            if s[i] == s[j]:
                if j - i < 2:  # Single character or adjacent characters are always palindromic
                    dp[i][j] = True
                elif not (i > 0 and dp[i-1][j-1]):
                    dp[i][j] = True
            if dp[i][j]:
                length = j - i + 1
                if length > max_len:
                    max_len = length
                    result = s[i:j+1]
    
    return result
