def numPathsWithKCoins(K, N):
    # Create a 2D DP table with size N x N and fill it with False values initially
    dp = [[False for _ in range(N)] for _ in range(N)]

    def dfs(i, j, remaining_coins):
        if i == N - 1 and j == N - 1:
            return remaining_coins == K

        # Check if the current cell has at least K - arr[i][j] coins left to collect
        if i < N - 1 or j < N - 1 and remaining_coins >= K - arr[i][j]:
            return dp[i][j]

        # If we haven't reached this cell before, calculate it and store the result in DP table
        if not dp[i][j]:
            if i + 1 < N:
                dp[i][j] = dfs(i + 1, j, remaining_coins - arr[i][j]) or (i == N - 2 and j < N - 1)
            if j + 1 < N:
                dp[i][j] = dfs(i, j + 1, remaining_coins - arr[i][j]) or (i < N - 1 and j == N - 2)

        return dp[i][j]

    # Initialize the base case
    dp[0][0] = True

    # Calculate the number of paths with exactly K coins
    result = sum(dfs(i, j, K) for i in range(N) for j in range(N))

    return result

# Test your code here
K = int(input())
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

print(numPathsWithKCoins(K, N))
