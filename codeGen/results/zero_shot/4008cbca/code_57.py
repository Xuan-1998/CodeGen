import sys

def solve(board, hand):
    result = 0
    for ball in board + hand:
        if ball in hand:  # inserting a new ball from hand
            result += 1
        else:  # updating an existing ball on board
            same_color_count = 0
            for i in range(len(board)):
                if board[i] == ball and (i < len(board) - 2 or ball != board[i-1] and board[i+2] != ball):
                    same_color_count += 1
            result -= same_color_count

    return -1 if any(c != ' ' for c in board) else result

# Example usage:
board = input().strip()
hand = input().strip()
print(solve(board, hand))
