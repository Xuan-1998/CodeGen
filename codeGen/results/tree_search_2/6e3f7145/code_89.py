def longest_palindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    max_length = 0
    result = ""
    
    for i in range(n):
        for j in range(i, n):
            if s[i] == s[j]:
                if j - i < 2:
                    dp[i][j] = True
                elif i > 0 and j < n-1:
                    dp[i][j] = (s[i-1] == s[j+1]) and dp[i-1][j+1]
                
                if dp[i][j]:
                    length = j - i + 1
                    if length > max_length:
                        max_length = length
                        result = s[i:j+1]
    
    return result

# Read input from standard input.
s = input()

print(longest_palindrome(s))
