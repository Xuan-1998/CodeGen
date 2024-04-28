def numPathsWithKCoins(K, N, arr):
    dp = [[0] * (N) for _ in range(N)]

    # Base case: when we're at the bottom right corner
    dp[N-1][N-1] = 1 if arr[N-1][N-1] == K else 0

    # Fill up the DP table from bottom to top and from left to right
    for i in range(N - 2, -1, -1):
        for j in range(N - 2, -1, -1):
            if arr[i][j] <= K:
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
            else:
                dp[i][j] = 0

    return dp[0][0]

K = int(input())
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

print(numPathsWithKCoins(K, N, arr))
