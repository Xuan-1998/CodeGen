def solve():
    K, N = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]
    dp[0][0][0] = 1
    
    for i in range(N):
        for j in range(N):
            if i > 0:
                dp[i][j][0] += dp[i-1][j][0]
            if j > 0:
                dp[i][j][0] += dp[i][j-1][0]
            if i < N-1 and j < N-1:
                for k in range(K):
                    dp[i+1][j][k+1] += dp[i][j][k]
                    dp[i][j+1][k+1] += dp[i][j][k]
    
    return dp[-1][-1][-1]

print(solve())
