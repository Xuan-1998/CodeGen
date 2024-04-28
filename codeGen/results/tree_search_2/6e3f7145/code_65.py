def longest_palindromic_substring(s):
    n = len(s)
    
    # Initialize the dp table with all False values
    dp = [[False] * n for _ in range(n)]
    
    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True
    
    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
    
    # Check for lengths greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # If the first and last characters match, check if the substring in between is a palindrome
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
    
    # Find the longest palindromic substring
    max_length = 0
    max_substring = ""
    
    for i in range(n):
        for j in range(i, n):
            if dp[i][j]:
                if j - i + 1 > max_length:
                    max_length = j - i + 1
                    max_substring = s[i:j+1]
    
    return max_substring

s = input()
print(longest_palindromic_substring(s))
