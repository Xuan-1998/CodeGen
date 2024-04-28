def solve():
    K, N = map(int, input().split())
    arr = []
    for _ in range(N):
        row = list(map(int, input().split()))
        arr.append(row)
    
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]
    dp[0][0][0] = arr[0][0]
    
    for i in range(N):
        for j in range(N):
            for k in range(K + 1):
                if i > 0:
                    dp[i][j][k] += dp[i-1][j][k]
                if j > 0:
                    dp[i][j][k] += dp[i][j-1][k]
                if i > 0 and j > 0:
                    dp[i][j][k] -= arr[i-1][j-1]
    return dp[-1][-1][K]
