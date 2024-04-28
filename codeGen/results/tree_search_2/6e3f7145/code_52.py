def longest_palindrome_substring(s):
    n = len(s)
    
    # Create a table to store whether each substring is a palindrome or not
    dp = [[False] * n for _ in range(n)]
    
    # Initialize the maximum length of palindromic substrings found so far
    max_length = 0
    
    # The longest palindromic substring ends at index i and has length 2i+1
    for center in range(n):
        for left in range(center, -1, -1):
            if s[left] == s[center]:
                if center-left <= 1:
                    dp[left][center] = True
                else:
                    dp[left][center] = dp[left+1][center-1]
                
                # Update the maximum length of palindromic substrings found so far
                if dp[left][center] and center - left + 1 > max_length:
                    max_length = center - left + 1
    
    return s[:max_length]
