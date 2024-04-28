def longest_palindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    # All substrings with one character are palindromes
    for i in range(n):
        dp[i][i] = True
    
    # Check for length 2 substrings
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
    
    # Check for lengths greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # If the first and last characters match and the substring in between is a palindrome
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
    
    # Find the longest palindromic substring
    max_length = 0
    longest_palindrome = ""
    
    for i in range(n):
        for j in range(i, n):
            if dp[i][j]:
                if j - i + 1 > max_length:
                    max_length = j - i + 1
                    longest_palindrome = s[i:j + 1]
    
    return longest_palindrome

# Test the function
s = input()
print(longest_palindrome(s))
