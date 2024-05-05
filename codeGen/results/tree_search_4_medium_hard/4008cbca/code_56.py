def min_moves_to_remove_all_balls(board, hand):
    dp = [[-1] * 6 for _ in range(len(board) + 1)]
    dp[0][0] = 0  # base case: no previous color

    for i in range(1, len(board) + 1):
        prev_color = board[i - 1]
        if i < len(hand):  # consider the first ball in the hand
            hand_colors = [c for c in hand if c != prev_color]
            min_moves = float('inf')
            for color in hand_colors:
                moves = dp[i - 1][ord(color) - ord('R')] + (i - 1 > 0)
                if moves < min_moves:
                    min_moves = moves
        else:  # no more balls in the hand
            min_moves = float('inf')

        for j, color in enumerate(['R', 'Y', 'B', 'G', 'W']):
            if (i > 1 and board[i - 2] == prev_color) or (prev_color != color and i > 0):
                dp[i][j] = min_moves
            else:
                dp[i][j] = dp[i - 1][ord(color) - ord('R')] + (i - 1 > 0)

    return min(dp[-1]) if any(dp[-1]) != -1 else -1

import sys
board = [input() for _ in range(20)]
hand = input()
print(min_moves_to_remove_all_balls(board, hand))
