S = input().strip()
T = input().strip()

def uncommon_subsequence(S, T):
    m = len(S)
    n = len(T)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    uncommon_length = m
    
    for i in range(m, -1, -1):
        for j in range(n, -1, -1):
            if S[i] == T[j]:
                uncommon_length = min(uncommon_length, dp[i - 1][j - 1] + 1)
                break
        else:
            continue
        break
    
    return max(0, m - uncommon_length)
