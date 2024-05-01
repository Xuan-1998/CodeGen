def numPathsWithKCoins(N, K, arr):
    dp = [[0] * (N) for _ in range(N)]

    # Initialize base case
    for j in range(N):
        if arr[0][j] <= K:
            dp[0][j] = 1
        else:
            dp[0][j] = 0

    # Fill up the rest of the table using dynamic programming
    for i in range(1, N):
        for j in range(N):
            if arr[i][j] <= K:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) if i > 0 and j > 0 else dp[i-1][j] if i > 0 else dp[i][j-1]
            else:
                if k - arr[i][j] >= 0:
                    dp[i][j] = (dp[i-1][j] + dp[i][j-1]) if i > 0 and j > 0 else dp[i-1][j] if i > 0 else dp[i][j-1]
                else:
                    dp[i][j] = 0

    return dp[N-1][N-1]

K, N = map(int, input().split())
arr = [[int(x) for x in input().split()] for _ in range(N)]

print(numPathsWithKCoins(N, K, arr))
