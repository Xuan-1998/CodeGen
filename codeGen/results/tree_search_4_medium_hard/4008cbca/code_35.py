def min_moves_to_remove_all_balls(board, hand):
    dp = {i: {-1: float('inf')} for i in range(len(board))}
    for i in range(len(board)):
        dp[i][0] = float('inf')
        for j in range(6):
            if board[i] == hand[j]:
                dp[i][j] = dp[i-1].get(j, -1) + 1
            elif j > 0:
                dp[i][j] = dp[i-1][k]
    return dp[len(board) - 1].get(5, -1)
