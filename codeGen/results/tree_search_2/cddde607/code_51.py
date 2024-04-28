def count_paths(arr, K):
    N = len(arr)
    dp = [[0] * (N) for _ in range(N)]

    # Base case: if it's possible to collect exactly K coins from cells (0, 0) to (N-1, N-1)
    dp[N-1][N-1] = 1 if sum(arr[0]) == K else 0

    for i in range(N):
        for j in range(N):
            # If there are enough coins in the current cell to reach the target
            if arr[i][j] <= K:
                # Consider two possibilities: moving down or moving right
                dp[i][j] = (dp[i+1][j] if i < N-1 else 0) + (dp[i][j+1] if j < N-1 else 0)
            # If there are not enough coins in the current cell to reach the target
            elif arr[i][j] > K:
                dp[i][j] = 0

    return dp[0][0]
