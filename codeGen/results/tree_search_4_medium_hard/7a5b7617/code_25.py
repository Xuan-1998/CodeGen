def dfs(i, j, s):
    if i == N:
        return 1 if s <= M else 0
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    res = 0
    for k in range(j+1):
        res += dfs(i-1, M-k-1, min(s, M)-k)
    dp[i][j] = res % (10**9 + 7)
    return dp[i][j]

N, M = map(int, input().split())
dp = [[-1 for _ in range(M+1)] for _ in range(N+1)]

print(dfs(N, M, N*M))
