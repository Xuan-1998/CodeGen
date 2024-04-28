def longest_palindrome(s):
    n = len(s)
    
    # Create a table to store results of subproblems
    dp = [[False] * n for _ in range(n)]
    
    # All substrings with one character are palindromes
    for i in range(n):
        dp[i][i] = True
    
    start, end = 0, 0
    
    # Check for substring of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start, end = i, i + 1
    
    # Check for lengths greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # If the first and last characters match and the substring in between is a palindrome
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                
                # Update the start and end indices for the longest palindromic substring found so far
                if length > (end - start):
                    start, end = i, j
    
    return s[start:end+1]

s = input()
print(longest_palindrome(s))
