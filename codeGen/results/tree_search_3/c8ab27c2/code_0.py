def uncommonFromSAndT(S, T):
    n, m = len(S), len(T)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = any(dp[k][j - 1] for k in range(i))
    
    for i in range(n + 1):
        if not any(dp[i][j] for j in range(m + 1)):
            return i
    return -1

S = input()
T = input()

print(uncommonFromSAndT(S, T))
