def count_paths(K, N, arr):
    # Initialize the 3D DP table
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]

    # Base case: when we're at the bottom-right corner and have exactly K coins
    dp[N-1][N-1][K] = 1

    # Fill up the DP table by considering all possible moves from each cell
    for i in range(N):
        for j in range(N):
            for k in range(K + 1):
                if i == N - 1 and j == N - 1:
                    continue  # Base case, we're already at the bottom-right corner

                # Calculate the number of valid paths to cell (i+1, j) with k-arr[i][j] coins
                left = dp[i+1][j][k-arr[i][j]] if k-arr[i][j] >= 0 else 0

                # Calculate the number of valid paths to cell (i, j+1) with k-arr[i][j] coins
                right = dp[i][j+1][k-arr[i][j]] if k-arr[i][j] >= 0 else 0

                # Update the DP table with the minimum of the two possibilities
                dp[i][j][k] = left + right

    # Return the number of valid paths to cell (0, 0) with exactly K coins
    return dp[0][0][K]
