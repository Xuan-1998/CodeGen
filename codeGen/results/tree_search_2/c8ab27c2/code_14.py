import sys

def shortest_common_subsequence(S, T):
    n = len(S)
    m = len(T)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                if i > 0 and j > 0:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                else:
                    dp[i][j] = 0

    for i in range(n, -1, -1):
        for j in range(m, -1, -1):
            if dp[i][j] == 0 and S[i:] != T[:j + 1]:
                return len(S) - i

    return -1

S = input()
T = input()

print(shortest_common_subsequence(S, T))
