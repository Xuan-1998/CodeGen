def min_portal_moves(n, portals):
    dp = [[float('inf')] * 3 for _ in range(n + 1)]

    dp[0][1] = 0

    for i in range(1, n + 1):
        p_i = portals[i - 1]
        if i % 2 == 1:
            # Use the second portal
            dp[i][2] = min(dp[p_i][1], dp[i][2])
        else:
            # Use the first portal
            dp[i][1] = min(dp[i - 1][1], dp[i][1]) + 1

    return (dp[n][0] + dp[n][1]) % 1000000007
