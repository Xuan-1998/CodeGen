import sys

def min_insertions(board, hand):
    insertions = 0
    for ball in hand:
        # Check if inserting the ball would remove any balls
        new_board = list(board)
        for i in range(len(new_board)):
            if new_board[i] == ball:
                new_board[i] = ''
        for i in range(len(new_board) - 2):
            if len(set([new_board[i], new_board[i+1], new_board[i+2]])) < 3:
                # Ball removed, update insertions
                insertions += 1
                break
    return insertions if all(ball == '' for ball in board) else -1

# Read input from stdin
board = input().strip()
hand = input().strip()

# Print the result to stdout
print(min_insertions(board, hand))
