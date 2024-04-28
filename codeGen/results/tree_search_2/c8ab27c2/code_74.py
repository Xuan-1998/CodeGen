def find_shortest_uncommon_subsequence():
    S, T = input().split(), input().split()
    m, n = len(S), len(T)
    dp = [[-1] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        if i == 0:
            dp[i][0] = 0
        else:
            dp[i][0] = -1

    for j in range(n + 1):
        if j == 0:
            dp[0][j] = 0
        else:
            dp[0][j] = -1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i-1] != T[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = -1
                for k in range(j+1):
                    dp[i][j] = min(dp[i][j], dp[i-1][k])

    return dp[m][n]

print(find_shortest_uncommon_subsequence())
