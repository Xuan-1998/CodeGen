def solve():
    K, N = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    dp = [[[0] * (K+1) for _ in range(N)] for _ in range(N)]

    dp[0][0][0] = 1
    
    for i in range(1, N):
        for j in range(i+1):
            for k in range(K+1):
                if arr[i][j] <= k:
                    dp[i][j][k] = (dp[i-1][j][k-arr[i][j]] if i > 0 else 0) + (dp[i][j-1][k-arr[i][j]] if j > 0 else 0)
                else:
                    dp[i][j][k] = 0
    
    print(dp[-1][-1][K])

solve()
