def solve():
    K, N = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]
    
    dp[0][0][0] = arr[0][0]
    
    for i in range(1, N):
        for j in range(N):
            if i == 0:
                dp[i][j][0] = arr[i][j]
            else:
                for k in range(K + 1):
                    dp[i][j][k] = max(dp[i-1][j][max(0, k-arr[i][j])], dp[i][j-1][max(0, k-arr[i][j])])
    
    return dp[-1][-1][-1]
