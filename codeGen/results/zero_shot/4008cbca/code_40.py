import sys

def remove_balls(board, hand):
    # Initialize the board state
    board_state = [c for c in board]

    # Sort the hand balls by color
    hand_sorted = sorted(set(hand))

    # Initialize the minimum number of moves needed to remove all balls
    min_moves = 0

    while True:
        # Find the first ball that can be removed
        i = 0
        while i < len(board_state):
            if board_state[i:i+3].count(board_state[i]) >= 3:
                del board_state[i:i+3]
                break
            i += 1

        # If no balls were removed, it's not possible to remove all the balls
        if i == len(board_state):
            return -1

        # Update the minimum number of moves needed
        min_moves += 1

    # Return the minimum number of moves needed to remove all balls
    return min_moves

# Read the input from stdin
board = sys.stdin.readline().strip()
hand = sys.stdin.readline().strip()

# Calculate the minimum number of moves needed to remove all balls
min_moves = remove_balls(board, hand)

# Print the result to stdout
print(min_moves)
