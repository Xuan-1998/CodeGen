def longest_palindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    # Initialize the diagonal to True, because a single character is always a palindrome.
    for i in range(n):
        dp[i][i] = True

    # Fill up the table. For each substring S[i...j], check if it's a palindrome.
    max_len = 0
    max_palindrome = ""
    
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            # If the characters at both ends are equal, and the substring in between is a palindrome,
            # then this whole substring is also a palindrome.
            if s[i] == s[j] and (j-i < 2 or dp[i+1][j-1]):
                dp[i][j] = True
                if j - i + 1 > max_len:
                    max_len = j - i + 1
                    max_palindrome = s[i:j+1]

    return max_palindrome

s = input()
print(longest_palindrome(s))
