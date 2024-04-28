def count_paths(k, n, arr):
    dp = [[[0] * (k+1) for _ in range(n)] for _ in range(n)]

    dp[0][0][0] = 1
    for i in range(1, n):
        if arr[i-1][0] <= k:
            dp[i][0][0] += dp[i-1][0][arr[i-1][0]]
        else:
            break

    for j in range(1, n):
        if arr[0][j] <= k:
            dp[0][j][0] += dp[0][j-1][arr[0][j]]
        else:
            break

    for i in range(1, n):
        for j in range(1, n):
            if arr[i][j] <= k:
                dp[i][j][0] = (dp[i-1][j][0] + dp[i][j-1][0]) if i > 0 and j > 0 else 0
                if arr[i-1][j] <= k:
                    dp[i][j][0] += dp[i-1][j][arr[i-1][j]]
                if arr[i][j-1] <= k:
                    dp[i][j][0] += dp[i][j-1][arr[i][j-1]]
            else:
                break

    return sum(sum(row) for row in dp[-1])
