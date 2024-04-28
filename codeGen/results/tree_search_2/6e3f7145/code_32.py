def longest_palindromic_substring(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    # Initialize the base case: single-character substrings are palindromes
    for i in range(n):
        dp[i][i] = True
    
    max_length = 0
    longest_palindrome = ""
    
    # Fill up the dynamic programming table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            if s[i] == s[j]:
                if length == 2 or dp[i+1][j-1]:
                    dp[i][j] = True
                    if length > max_length:
                        max_length = length
                        longest_palindrome = s[i:j+1]
    
    return longest_palindrome

s = input()
print(longest_palindromic_substring(s))
