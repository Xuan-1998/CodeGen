def maxScore(arr, k, z):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    visited = set()

    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if i == 1:
                dp[i][j] = arr[0]
            elif j > 0 and (i - 1 not in visited or len(visited) < z):
                # Move left
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + arr[i-1])
                visited.add(i)
            if i <= n and j > 0:
                # Move right
                dp[i][j] = max(dp[i][j], dp[i+1][j-1] + arr[i])

    return dp[1][k]
