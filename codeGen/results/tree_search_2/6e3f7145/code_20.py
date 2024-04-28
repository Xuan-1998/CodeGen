def longest_palindromic_substring(S):
    n = len(S)
    dp = [[False] * n for _ in range(n)]
    
    max_length = 0
    center_index = 0
    
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if S[i] == S[j] and (j - i < 3 or dp[i + 1][j - 1]):
                dp[i][j] = True
                if j - i > max_length:
                    max_length = j - i
                    center_index = i
    
    return S[center_index:center_index + max_length]
