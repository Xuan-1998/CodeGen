def findUncommonSubsequence(S, T):
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = i
            elif S[i - 1] != T[j - 1]:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
            else:
                dp[i][j] = dp[i - 1][j - 1]

    for i in range(m, -1, -1):
        for j in range(n, -1, -1):
            if S[i] != T[j]:
                return n - j

    return -1

S, T = input().split()
print(findUncommonSubsequence(S, T))
