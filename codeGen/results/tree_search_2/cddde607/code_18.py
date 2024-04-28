def count_paths(K, N, arr):
    # Create a 2D DP table with dimensions (N x N)
    dp = [[0] * N for _ in range(N)]

    # Base case: only one way to collect exactly K coins from the top left corner
    dp[0][0] = 1 if arr[0][0] == K else 0

    # Fill up the DP table
    for i in range(1, N):
        for j in range(N):
            # If we're at the bottom row or rightmost column, there's only one way to collect exactly K coins
            if i == N - 1 and j > 0:
                dp[i][j] = dp[i][j - 1]
            elif j == N - 1 and i > 0:
                dp[i][j] = dp[i - 1][j]
            else:
                # If we're not at the boundary, consider moving down or right
                if arr[i][j] <= K:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0

    return dp[N - 1][N - 1]

# Example usage:
K, N = map(int, input().split())
arr = [[int(x) for x in input().split()] for _ in range(N)]

print(count_paths(K, N, arr))
