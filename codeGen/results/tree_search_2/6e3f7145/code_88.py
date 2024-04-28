def longest_palindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    # Initialize the diagonal elements to True, since single characters are always palindromes
    for i in range(n):
        dp[i][i] = True
    
    max_length = 1
    longest_palindrome = s[0]
    
    # Fill up the dp table in a bottom-up manner
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # Check if the substring S[i..j] is a palindrome
            if s[i] == s[j]:
                if length == 2 or dp[i+1][j-1]:
                    dp[i][j] = True
                    
                    # Update the longest palindromic substring if necessary
                    if length > max_length:
                        max_length = length
                        longest_palindrome = s[i:j+1]
    
    return longest_palindrome

# Test the function
s = input()
print(longest_palindrome(s))
