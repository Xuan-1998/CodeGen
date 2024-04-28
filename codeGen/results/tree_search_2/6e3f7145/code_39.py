def longest_palindromic_substring(s):
    n = len(s)
    
    # Initialize a 2D array to store the dynamic programming table.
    dp = [[False] * n for _ in range(n)]
    
    # All substrings with one character are palindromes.
    max_length = 1
    for i in range(n):
        dp[i][i] = True
    
    # Check for lengths 2,3,... and store the results in a table.
    start = 0
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # If the substring is palindromic then mark it as True in dp.
            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i+1][j-1]
                
                # Update the maximum length of a palindromic substring.
                if dp[i][j]:
                    start = i
                    max_length = length
    
    return s[start:start + max_length]

s = input()
print(longest_palindromic_substring(s))
