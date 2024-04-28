def numPathsToCollectExactlyKCoins(arr):
    N = len(arr)
    K = int(input())  # read K from standard input

    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                if arr[i][j] <= K:
                    dp[i][j][arr[i][j]] = 1
            elif i > 0 and j > 0:
                dp[i][j][K] += min(dp[i-1][j][K-arr[i-1][j]], dp[i][j-1][K-arr[i][j-1]])

    return dp[N-1][N-1][K]

print(numPathsToCollectExactlyKCoins([list(map(int, input().split())) for _ in range(int(input()))]))
