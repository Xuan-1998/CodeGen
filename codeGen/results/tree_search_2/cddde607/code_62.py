def count_paths(K, N, arr):
    dp = [[False] * (N) for _ in range(N)]

    # Base case: if K is 0, it's possible to collect exactly 0 coins by not moving at all
    dp[0][0] = True

    for i in range(N):
        for j in range(N):
            if arr[i][j] <= K and (i == N-1 or j == N-1):
                # If we're at the bottom row or rightmost column, we can collect exactly K coins
                dp[i][j] = True

            if i > 0:
                # Update the cell above us
                if dp[i-1][j]:
                    dp[i][j] = dp[i][j] or (arr[i-1][j] <= K - arr[i][j])

            if j > 0:
                # Update the cell to our left
                if dp[i][j-1]:
                    dp[i][j] = dp[i][j] or (arr[i][j-1] <= K - arr[i][j])

    return int(sum(1 for i in range(N) for j in range(N) if dp[i][j] and arr[i][j] == K))
