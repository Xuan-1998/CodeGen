import sys

def uncommon_subsequence(S, T):
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    uncommon_len = float('inf')
    for i in range(m + 1):
        for j in range(n + 1):
            if S[i:] != T[j:]:
                uncommon_len = min(uncommon_len, i - j)

    return -1 if uncommon_len == float('inf') else uncommon_len

S, T = input().split()
print(uncommon_subsequence(S, T))
