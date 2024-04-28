import sys

def uncommon_subsequence(S, T):
    n = len(S)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i):
            if S[j:i].find(T) == -1:  # S[:i] is not a subsequence in T
                dp[i] = 1
                break
        else:
            lcs = longest_common_subsequence(S[:i-1], T)
            dp[i] = 1 + min(dp[i-1], lcs)

    return dp[n]

def longest_common_subsequence(S, T):
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i-1] == T[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

S, T = input().split()
result = uncommon_subsequence(S, T)
print(result)
