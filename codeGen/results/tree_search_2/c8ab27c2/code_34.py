def findShortestSubArray(S, T):
    n = len(S)
    m = len(T)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if S[i - 1] not in T[:j]:
                dp[i][j] = dp[i - 1][j] + 1
            elif T[j - 1] not in S[:i]:
                dp[i][j] = dp[i][j - 1] + 1
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]

S, T = input().split()
print(findShortestSubArray(S, T))
