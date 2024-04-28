def longest_palindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    max_len = 0
    max_palindrome = ""
    
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j]:
                if j - i < 2:
                    dp[i][j] = True
                elif j - i == 2:
                    dp[i][j] = (s[i] == s[j-1])
                else:
                    dp[i][j] = dp[i+1][j-1]
                if dp[i][j]:
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        max_palindrome = s[i:j+1]
    return max_palindrome

s = input()
print(longest_palindrome(s))
