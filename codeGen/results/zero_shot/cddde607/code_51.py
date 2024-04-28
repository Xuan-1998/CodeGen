def solve():
    K, N = map(int, input().split())
    arr = [[*map(int, input().split())] for _ in range(N)]
    dp = [[[0]*(K+1) for _ in range(N)] for _ in range(N)]

    dp[0][0][0] = 1 if arr[0][0] <= K else 0
    for i in range(1, N):
        dp[i][0][0] = 0
    for j in range(1, N):
        dp[0][j][0] = 0

    for i in range(1, N):
        for j in range(N):
            for k in range(K+1):
                if arr[i][j] <= k:
                    dp[i][j][k] = (dp[i-1][j][k-arr[i][j]] if i > 0 else 0) + (dp[i][j-1][k-arr[i][j]] if j > 0 else 0)
                else:
                    dp[i][j][k] = 0

    return dp[N-1][N-1][K]
