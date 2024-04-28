s = input()
t = input()

def shortest_uncommon_subsequence(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    uncommon_subsequence_length = 0
    for i in range(m, -1, -1):
        if dp[i][n] != dp[m][n]:
            uncommon_subsequence_length += 1
            break
    
    return uncommon_subsequence_length

print(shortest_uncommon_subsequence(s, t))
