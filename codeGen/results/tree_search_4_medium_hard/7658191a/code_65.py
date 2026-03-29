def max_score(n, k, z):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    left_moves = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if i <= k:
            dp[i][i - 1] = array[i - 1]
        for j in range(min(i, k), -1, -1):
            if left_moves[j]:
                dp[i][j] = max(dp[i-1][max(0, j-z)], dp[i-1][j-1] + array[i])
                left_moves[j] = (left_moves[j] + 1) % z
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + array[i])
    
    return dp[n][0]
