def numPaths(arr, K):
    N = len(arr)
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]

    # Initialize base cases
    for k in range(K + 1):
        dp[0][0][k] = 1 if k == 0 else 0

    # Fill up the DP table
    for i in range(N):
        for j in range(N):
            for k in range(K + 1):
                if arr[i][j] > 0:
                    dp[i][j][k] = 0
                elif i == N - 1 and j == N - 1:
                    dp[i][j][k] = 1 if k == 0 else 0
                else:
                    if i < N - 1:
                        dp[i][j][k] += dp[i + 1][j][max(k - arr[i][j], 0)]
                    if j < N - 1:
                        dp[i][j][k] += dp[i][j + 1][max(k - arr[i][j], 0)]

    # Return the answer
    return dp[0][0][K]

# Example usage:
K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(numPaths(arr, K))
