from collections import defaultdict

def num_paths_with_k_coins(K, N, arr):
    # Create a dictionary to store the DP states
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]

    # Initialize the base cases
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                dp[i][j][arr[0][0]] = 1
            elif i == 0:
                dp[i][j][arr[0][j]] += dp[i][j-1][arr[0][j-1]]
            elif j == 0:
                dp[i][j][arr[i][0]] += dp[i-1][j][arr[i-1][0]]

    # Fill the DP table
    for i in range(1, N):
        for j in range(1, N):
            for k in range(K + 1):
                if k >= arr[i][j]:
                    dp[i][j][k] = sum(dp[i-1][j][k-coin] for coin in range(arr[i][j]+1)) + \
                                   sum(dp[i][j-1][k-coin] for coin in range(arr[i][j]+1))
                else:
                    dp[i][j][k] = 0

    # Return the result
    return dp[N-1][N-1][K]

# Test your function
K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(num_paths_with_k_coins(K, N, arr))
