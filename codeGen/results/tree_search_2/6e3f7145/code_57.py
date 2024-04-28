def longest_palindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    # Base case: single characters are palindromes
    for i in range(n):
        dp[i][i] = True
    
    # Expand from base case to find longer palindromes
    max_length = 1
    result = s[0]
    for i in range(n-1):
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = (i+1 < j and dp[i+1][j-1]) or (i == j and True)
                if not dp[i][j]:
                    continue
                length = j - i + 1
                if length > max_length:
                    max_length = length
                    result = s[i:j+1]
    
    return result

