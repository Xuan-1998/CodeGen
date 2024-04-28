def longest_palindrome(s):
    # Initialize a 2D array to store whether each substring is palindromic or not
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    # All substrings of length 1 are palindromes
    max_len = 0
    max_palindrome = ""
    
    for i in range(n):
        dp[i][i] = True
    
    # Fill the table in a bottom-up manner
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            
            # If the substring has only one character or is of length 2 and characters are same,
            # then it's a palindrome
            if cl == 2:
                dp[i][j] = (s[i] == s[j])
            else:
                dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])
            
            # If the substring is palindromic, update the maximum length palindrome found so far
            if dp[i][j]:
                if cl > max_len:
                    max_len = cl
                    max_palindrome = s[i:j+1]
    
    return max_palindrome

# Read the input string from standard input
s = input()

print(longest_palindrome(s))
