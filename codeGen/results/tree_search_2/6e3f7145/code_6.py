def longest_palindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    max_len = 0
    result = ""
    
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j]:
                if j - i < 2:
                    dp[i][j] = True
                elif dp[i + 1][j - 1]:
                    dp[i][j] = True
                
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    result = s[i:j+1]
    
    return result

s = input()
print(longest_palindrome(s))
