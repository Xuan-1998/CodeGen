import sys

def uncommon_subsequence_length(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_length = dp[m][n]
    uncommon_length = m - lcs_length if lcs_length > 0 else -1

    return uncommon_length

s, t = input().split()
print(uncommon_subsequence_length(s, t))
