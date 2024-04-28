def shortest_uncommon_subsequence():
    S = input().strip()
    T = input().strip()

    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 and j == 0:
                continue
            elif S[i-1] != T[j-1]:
                dp[i][j] = 1
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

    return dp[m][n]

print(shortest_uncommon_subsequence())
