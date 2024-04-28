def longest_palindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    # Initialize diagonal elements to True (single-character substrings are palindromes)
    for i in range(n):
        dp[i][i] = True
    
    # Fill up the dp table
    max_length = 0
    result = ""
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                dp[i][j] = True
                if j - i + 1 > max_length:
                    max_length = j - i + 1
                    result = s[i:j+1]
    
    return result

s = input()
print(longest_palindrome(s))
