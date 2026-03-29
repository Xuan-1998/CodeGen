def min_moves_to_remove_boards(board, hand):
    dp = [[float('inf')] * (len(hand) + 1) for _ in range(len(board) + 1)]
    dp[0] = [i for i in range(len(hand) + 1)]  # base case: no balls on the board

    for i in range(1, len(board) + 1):
        for j in range(1, min(i + 1, len(hand) + 1)):
            if board[i - 1] == hand[j - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)
            else:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)

    return -1 if dp[-1][-1] == float('inf') else dp[-1][-1]
