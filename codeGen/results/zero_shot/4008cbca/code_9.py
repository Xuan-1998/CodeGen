import sys

# Read input from stdin
board = sys.stdin.readline().strip()
hand = sys.stdin.readline().strip()

# Initialize a set to store the colors of the balls in hand
colors_in_hand = set(hand)

# Initialize a variable to store the minimum number of balls needed to remove all the balls
min_balls_needed = 0

# Iterate over each ball on the board
for i, ball in enumerate(board):
    # If this is not the first ball and it has the same color as the previous ball,
    # we don't need to insert any more balls because they will be removed anyway
    if i > 0 and ball == board[i-1]:
        continue

    # Check if there are three or more balls of the same color touching this ball
    if (ball in colors_in_hand) and (i + 2 < len(board) and board[i+1] == ball and board[i+2] == ball):
        min_balls_needed = -1
        break

    # If there are no three or more balls of the same color touching this ball,
    # we need to insert one more ball to remove it
    if (ball in colors_in_hand) and (i + 2 < len(board)):
        continue

    # Increment the minimum number of balls needed
    min_balls_needed += 1

# Print the result to stdout
print(min_balls_needed)
