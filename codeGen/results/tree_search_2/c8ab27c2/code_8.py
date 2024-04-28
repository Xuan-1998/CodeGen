from collections import defaultdict

def shortest_common_subsequence(S, T):
    n = len(S)
    m = len(T)

    dp = [[False for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if S[i-1] == T[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = (dp[i-1][j] or dp[i][j-1])

    for i in range(n, -1, -1):
        for j in range(m, -1, -1):
            if not dp[i][j]:
                return i

    return -1

S = input().strip()
T = input().strip()

print(shortest_common_subsequence(S, T))
