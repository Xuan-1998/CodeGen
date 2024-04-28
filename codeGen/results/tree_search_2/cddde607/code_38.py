def numPathsWithKCoins(K, N, arr):
    dp = [[[0] * (K+1) for _ in range(N)] for _ in range(N)]

    # Base case
    dp[N-1][N-1][K] = 1 if arr[N-1][N-1] <= K else 0

    for i in range(N-2, -1, -1):
        for j in range(N-2, -1, -1):
            for k in range(K+1):
                if k < arr[i][j]:
                    dp[i][j][k] = 0
                elif k == arr[i][j]:
                    dp[i][j][k] = 1
                else:
                    dp[i][j][k] = dp[i-1][j][k-arr[i][j]] + dp[i][j-1][k-arr[i][j]]

    return dp[0][0][K]

# Example usage
K, N = map(int, input().split())
arr = [[int(x) for x in input().split()] for _ in range(N)]
print(numPathsWithKCoins(K, N, arr))
