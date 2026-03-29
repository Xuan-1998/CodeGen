def min_moves_to_remove_all_balls(board, hand):
    # Initialize dynamic programming table
    dp = [[float('inf')] * (len(hand) + 1) for _ in range(len(board) + 1)]

    # Base case: When the board is empty, it takes 0 moves to remove all balls.
    dp[0][0] = 0

    for i in range(1, len(board) + 1):
        for j in range(i + 1):
            # Check if there are three or more consecutive balls with the same color
            if board[i - 1] == board[max(j - 3, 0)] and board[i - 1] != ' ':
                dp[i][j] = min(dp[i][j], dp[i - 1][max(0, j - 4)] + 1)
            else:
                # Choose the option that requires the fewest moves
                dp[i][j] = min(dp[i][j], dp[i - 1][j])

    # Return the minimum number of moves needed to remove all balls on the board.
    return dp[-1][-1]

# Example usage
board = input().strip()
hand = input().strip()
print(min_moves_to_remove_all_balls(board, hand))
