def shortest_uncommon_subsequence(S, T):
    n, m = len(S), len(T)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    min_length = float('inf')
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if S[i - 1] != T[j - 1]:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j])
            else:
                dp[i][j] = 0
            
            # Update the minimum length
            if dp[i][j] == 1 and i < n and j < m:
                min_length = min(min_length, i + j)
    
    return min_length if min_length != float('inf') else -1
