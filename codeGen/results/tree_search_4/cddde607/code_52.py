def numPaths(arr, N, K):
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == N - 1 and j == N - 1:
                if arr[i][j] == K:
                    dp[i][j][K] = 1
                else:
                    dp[i][j][K] = 0
            elif i < N - 1 or j < N - 1:
                if i < N - 1 and j < N - 1:
                    for k in range(min(K, arr[i][j]) + 1):
                        dp[i][j][k] = (dp[i+1][j][k-arr[i][j]] +
                                        dp[i][j+1][k-arr[i][j]])
                elif i < N - 1:
                    for k in range(min(K, arr[i][j]) + 1):
                        dp[i][j][k] = (dp[i+1][j][k-arr[i][j]] +
                                        dp[i][j][k-arr[i][j]])
                else:  # j < N - 1
                    for k in range(min(K, arr[i][j]) + 1):
                        dp[i][j][k] = (dp[i][j+1][k-arr[i][j]] +
                                        dp[i][j][k-arr[i][j]])

    return dp[0][0][K]

# Example usage
K = int(input())
N = int(input())
arr = [[int(x) for x in input().split()] for _ in range(N)]
print(numPaths(arr, N, K))
