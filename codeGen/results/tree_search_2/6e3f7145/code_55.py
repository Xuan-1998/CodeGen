def longest_palindromic_substring(S):
    n = len(S)
    dp = [[0] * n for _ in range(n)]
    
    # Initialize the diagonal (single-character palindromes)
    for i in range(n):
        dp[i][i] = 1
    
    max_len = 0
    start_idx = 0
    
    # Fill in the DP table
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if S[i] == S[j]:
                if i+1 == j or dp[i+1][j-1]:
                    dp[i][j] = 1
                    if j-i+1 > max_len:
                        max_len = j-i+1
                        start_idx = i
    
    return S[start_idx:start_idx+max_len]
