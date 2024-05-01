def numPaths(arr, N, K):
    dp = [[[0] * (K+1) for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                dp[i][j][0] = arr[0][0]
            elif i == 0:
                dp[i][j][0] = dp[i][j-1][0]
            elif j == 0:
                dp[i][j][0] = dp[i-1][j][0]
            else:
                for k in range(K+1):
                    if arr[i][j] <= k:
                        dp[i][j][k] = (dp[i-1][j][k-arr[i][j]] + dp[i][j-1][k-arr[i][j]]) if i > 0 and j > 0 else 0

    return sum([sum(row) for row in dp[-1]])

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(numPaths(arr, N, K))
