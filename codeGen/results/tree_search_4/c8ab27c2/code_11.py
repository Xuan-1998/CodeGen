from collections import defaultdict

def find_shortest_uncommon_subsequence(S, T):
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize DP table with zeros
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
                
    # Fill up the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
                
    # Find the minimum length uncommon subsequence
    min_length = m
    for i in range(m, -1, -1):
        for j in range(n, -1, -1):
            if S[i] != T[j]:
                min_length = min(min_length, dp[i][j])
                
    return min_length

S = input()
T = input()
print(find_shortest_uncommon_subsequence(S, T))
