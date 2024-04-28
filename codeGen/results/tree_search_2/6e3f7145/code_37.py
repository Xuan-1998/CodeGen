def longest_palindromic_substring(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    # Initialize the diagonal elements as True, since single characters are always palindromes
    for i in range(n):
        dp[i][i] = True
    
    # Build up the solution by considering all possible substrings
    max_length = 0
    longest_substring = ""
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # Check if the substring is a palindrome
            if s[i] == s[j] and (length == 2 or dp[i+1][j-1]):
                dp[i][j] = True
                
                # Update the maximum length and the longest palindromic substring if necessary
                if length > max_length:
                    max_length = length
                    longest_substring = s[i:j+1]
    
    return longest_substring

# Read input from stdin and print the result to stdout
s = input()
print(longest_palindromic_substring(s))
