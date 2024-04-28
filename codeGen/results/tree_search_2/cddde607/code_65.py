def numPathsWithKCoins(K, N, arr):
    dp = [[False for _ in range(N)] for _ in range(N)]

    # Base case: dp[N-1][N-1] is True if it's possible to collect exactly K coins from cells (0, 0) to (N-1, N-1)
    dp[N-1][N-1] = arr[0][0] == K

    for i in range(N):
        for j in range(N):
            # If we're at the last row or column, it's always possible to reach this cell with exactly K coins
            if i == N-1 or j == N-1:
                dp[i][j] = arr[i][j] <= K
            else:
                # Calculate the number of coins left to collect in the current cell
                coinsLeft = K - arr[i][j]
                # If we can reach this cell with exactly K coins, it means we've already collected all the coins
                if coinsLeft >= 0:
                    dp[i][j] = (dp[i-1][j] if i > 0 else True) and (dp[i][j-1] if j > 0 else True)

    # Return the value at the bottom-right cell, which represents whether it's possible to collect exactly K coins
    return dp[N-1][N-1]

# Example usage:
K = int(input())  # Read K from standard input
N = int(input())  # Read N from standard input
arr = [[int(x) for x in input().split()] for _ in range(N)]  # Read the 2D array from standard input

result = numPathsWithKCoins(K, N, arr)
print(result)  # Print the result to standard output
