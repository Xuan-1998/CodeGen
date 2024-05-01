from collections import defaultdict

def find_shortest_uncommon_subsequence():
    S, T = input().strip().split()
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    uncommon_lengths = []
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            
            if i < m and j < n and S[i] != T[j]:
                uncommon_lengths.append(i)
    
    return min(uncommon_lengths) if uncommon_lengths else -1

print(find_shortest_uncommon_subsequence())
