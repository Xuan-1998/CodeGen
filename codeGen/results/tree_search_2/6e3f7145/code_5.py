def longest_palindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    max_length = 0
    start_index = 0
    
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1]):
                dp[i][j] = True
                if j - i > max_length:
                    max_length = j - i
                    start_index = i
    
    return s[start_index:start_index + max_length]

s = input()
print(longest_palindrome(s))
