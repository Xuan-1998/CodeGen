S = input().strip()
T = input().strip()

def uncommon_subsequence_length(S, T):
    n, m = len(S), len(T)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    uncommon_length = 0
    i, j = n, m
    while i > 0 and j > 0:
        if S[i - 1] == T[j - 1]:
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            j -= 1
            uncommon_length += 1
    
    return max(0, n + m - 2 * (uncommon_length or 0))
