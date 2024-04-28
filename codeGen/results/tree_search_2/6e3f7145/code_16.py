def longest_palindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    # Initialize the diagonal elements as True, since single characters are palindromes
    for i in range(n):
        dp[i][i] = True
    
    max_length = 0
    start = 0
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            # If the characters at positions i and j are the same
            if s[i] == s[j]:
                # And the substring between them is a palindrome
                if j - i < 3 or dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if j - i > max_length:
                        max_length = j - i
                        start = i
    
    return s[start:start + max_length]
