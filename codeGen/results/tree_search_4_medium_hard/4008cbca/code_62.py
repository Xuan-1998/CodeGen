def min_moves_to_remove_all_balls(board, hand):
    n = len(board)
    min_moves = [0] * (n + 1)  # Initialize the minimum number of moves needed to remove all balls up to each position

    prev_color = None
    for i in range(n):
        if board[i] != prev_color:  # If the current color is different from the previous one
            min_moves[i+1] = min_moves[i] + 1  # The minimum number of moves needed at this position is equal to the minimum number of moves needed at the previous position plus 1
        elif i >= 2 and board[i-2:i+1].count(board[i]) >= 3:  # If there are three or more consecutive balls with the same color
            min_moves[i+1] = min_moves[i] + 1  # The minimum number of moves needed at this position is equal to the minimum number of moves needed at the previous position plus 1
        else:
            min_moves[i+1] = min_moves[i]  # No new balls are added, so we can keep removing them as before

    if len(hand) > 0:  # If there are still balls in hand
        return -1  # It's not possible to remove all the balls
    else:
        return min_moves[-1]  # Return the minimum number of moves needed to remove all balls on the board


# Example usage
board = input().strip()
hand = input().strip()
print(min_moves_to_remove_all_balls(board, hand))
