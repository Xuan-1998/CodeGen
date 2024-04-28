def longest_palindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    max_length = 0
    start = 0
    
    for i in range(n):
        dp[i][i] = True
        max_length = 1
        start = i
        
        for j in range(i - 1, -1, -1):
            if s[j] == s[i]:
                if i - j < 2 or dp[j + 1][i - 1]:
                    dp[j][i] = True
                    if i - j > max_length:
                        max_length = i - j
                        start = j
    
    return s[start:start + max_length]

s = input()
print(longest_palindrome(s))
