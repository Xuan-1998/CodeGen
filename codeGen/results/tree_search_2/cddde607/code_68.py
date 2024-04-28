def numPathsWithKCoins(K, N, arr):
    dp = [[[False] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]

    # Base case: reaching the bottom-right cell with exactly K coins
    dp[N-1][N-1][0] = arr[0][0] == K

    for i in range(N - 2, -1, -1):
        for j in range(N - 2, -1, -1):
            if arr[i][j] <= K:
                dp[i][j][K] = (dp[i+1][j][max(0, K-arr[i][j])] or
                                 dp[i][j+1][max(0, K-arr[i][j])])

    # Count the number of paths that collect exactly K coins
    return sum([dp[0][N-1][k] for k in range(K+1)])

# Example usage:
K = int(input())
N = int(input())
arr = [[int(x) for x in input().split()] for _ in range(N)]

print(numPathsWithKCoins(K, N, arr))
