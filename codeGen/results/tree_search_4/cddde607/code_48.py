def numPaths(arr):
    N = len(arr)
    K = int(input())

    # Initialize dp table with zeros
    dp = [[[0 for _ in range(K + 1)] for _ in range(N)] for _ in range(N)]

    # Set up base case: there's only one way to reach the top-left corner (i.e., take no coins)
    dp[0][0][0] = 1

    for i in range(N):
        for j in range(N):
            if i > 0:
                for k in range(min(K, arr[i][j]) + 1):
                    dp[i][j][k] += dp[i-1][j][k]
            if j > 0:
                for k in range(max(0, K - arr[i][j]) + 1):
                    dp[i][j][k] += dp[i][j-1][k]

    return dp[N-1][N-1][K]

# Test your function
arr = [[int(x) for x in input().split()] for _ in range(int(input()))]
print(numPaths(arr))
