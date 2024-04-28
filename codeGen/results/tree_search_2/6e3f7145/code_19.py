def longest_palindrome(s):
    n = len(s)
    
    # Create a table to store the lengths of palindromic substrings
    dp = [[0] * n for _ in range(n)]
    
    # Initialize the diagonal elements as 1, since single characters are palindromes
    for i in range(n):
        dp[i][i] = 1
    
    # Fill up the table in a bottom-up manner
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            
            # Check if the substring is palindromic
            if s[i] == s[j]:
                if cl == 2:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i + 1][j - 1]
            
    # Find the maximum length of a palindromic substring
    max_length = 0
    for i in range(n):
        for j in range(i, n):
            if dp[i][j] > max_length:
                max_length = dp[i][j]
    
    return s[:max_length + 1]

# Read the input string from standard input
s = input()

# Print the longest palindromic substring
print(longest_palindrome(s))
