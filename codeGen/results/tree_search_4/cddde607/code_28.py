def numPathsThatCollectExactlyKCoins(K, N, arr):
    dp = [[0] * (N) for _ in range(N)]

    # Base case: Initialize the first row and column
    dp[0][0] = 1 if arr[0][0] <= K else 0

    # Fill up the table using memoization
    for i in range(1, N):
        for j in range(N):
            if arr[i][j] <= K:
                if i == 0:  # First row
                    dp[i][j] = dp[i][j-1] if j > 0 else 1
                elif j == 0:  # First column
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[N-1][N-1]

K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = numPathsThatCollectExactlyKCoins(K, N, arr)
print(result)
