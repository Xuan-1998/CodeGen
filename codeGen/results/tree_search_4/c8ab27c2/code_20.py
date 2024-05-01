def shortest_common_subsequence(S, T):
    n, m = len(S), len(T)
    dp = [[-1] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 and j == 0:
                continue
            if S[i - 1] == T[j - 1]:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    if dp[n][m] == -1:
        return -1
    return n - dp[n][m]

S, T = input().split()
print(shortest_common_subsequence(S, T))
