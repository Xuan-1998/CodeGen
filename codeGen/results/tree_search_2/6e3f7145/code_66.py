code
def longest_palindromic_substring(s):
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]
    
    max_len = 0
    start_idx = 0
    
    for i in range(n):
        for j in range(i, n):
            if s[i] == s[j]:
                if j - i < 2:  # Single character or two characters are always palindromes
                    dp[i][j] = True
                elif i > 0 and j < n-1:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = True
                
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    start_idx = i
    
    return s[start_idx:start_idx+max_len]

print(longest_palindromic_substring(input()))
