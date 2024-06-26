code block
def longest_palindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = True  # Single characters are palindromes
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = False
    
    max_length = 0
    result = ""
    
    for i in range(n):
        for j in range(i, n):
            if dp[i][j]:
                length = j - i + 1
                if length > max_length:
                    max_length = length
                    result = s[i:j+1]
    
    return result
