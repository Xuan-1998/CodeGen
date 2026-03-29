dp = [[0] * (C + 1) for _ in range(C + 1)]

for i in range(1, C + 1):
    dp[i][0] = 0
    for j in range(i):
        if i > 1:
            dp[i][j] += min(dp[j][j-1], dp[j-1][j])
        else:
            dp[i][j] = 1
        dp[i][i] = sum(dp[k][i-1] for k in range(j, i))

for _ in range(T):
    N, M, C = map(int, input().split())
    U = list(map(int, input().split()))
    L = list(map(int, input().split()))
    
    res = [0] * (C + 1)
    for i in range(N):
        res[U[i]] += dp[U[i]][U[i]-1]
    for i in range(M):
        res[L[i]] += dp[L[i]][L[i]-1]
    
    print(*res, sep=' ')
