def min_moves_to_remove_balls(board, hand):
    n = len(board)
    dp = [[float('inf')] * (len(hand) + 1) for _ in range(n + 1)]
    dp[0] = [0] * (len(hand) + 1)

    for i in range(1, n + 1):
        prev_color = board[i - 1]
        if i < n and prev_color == board[i]:
            for j in range(len(hand)):
                if hand[j] != prev_color:
                    dp[i][j + 1] = min(dp[i][j + 1], dp[i - 1][j] + 1)
        else:
            for j in range(len(hand) + 1):
                dp[i][j] = dp[i - 1][j]

    return min(dp[n]) if dp[n] != [float('inf')] * (len(hand) + 1) else -1
