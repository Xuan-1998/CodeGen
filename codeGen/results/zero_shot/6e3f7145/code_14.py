def longest_palindromic_substring(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    max_len = 0
    start = 0
    
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j]:
                if j-i < 2:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i+1][j-1]
                
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    start = i
                    
    return s[start:start+max_len]

s = input()
print(longest_palindromic_substring(s))
