def min_moves(board, hand):
    n = len(board)
    m = len(hand)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == n:
                dp[i][j] = min(j, m)
            elif j >= 3 and i >= 3:
                dp[i][j] = min(1 + dp[i - 1][j], 3 + dp[i - 4][j - 3])
            else:
                dp[i][j] = min(j, m)

    return dp[n][m]
