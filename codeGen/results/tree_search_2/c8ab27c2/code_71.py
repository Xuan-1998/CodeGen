import sys

def shortest_uncommon_subsequence():
    S = input().strip()
    T = input().strip()

    m, n = len(S), len(T)
    dp = [[-1] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = -1
            elif j == 0:
                dp[i][j] = i
            else:
                if S[i - 1] == T[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    min_len = m + 1
                    for k in range(j, -1, -1):
                        if S[i - 1] != T[k - 1]:
                            min_len = min(min_len, dp[i - 1][k])
                    dp[i][j] = min_len

    return dp[m][n]

print(shortest_uncommon_subsequence())
