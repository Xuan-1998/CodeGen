def longest_palindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    max_length = 0
    start_index = 0
    
    for i in range(n):
        for j in range(i, n):
            if s[i] == s[j]:
                if i + 1 > j - 1 or dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if j - i + 1 > max_length:
                        max_length = j - i + 1
                        start_index = i
    return s[start_index:start_index+max_length]

s = input()
print(longest_palindrome(s))
