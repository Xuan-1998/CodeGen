import sys

def solve(board, hand):
    while True:
        # Find positions where we can insert a ball from our hand
        for i in range(len(board)):
            if board[i] == 'R' and hand[0] == 'B':
                return i  # insert blue ball at this position
            elif board[i] == 'Y' and hand[0] == 'G':
                return i  # insert green ball at this position
            # ... handle other colors ...
        
        if not any(board[i] == c for c in hand):
            break  # no more balls to insert, so stop

    return -1  # it's not possible to remove all balls

# Read input from stdin
board = sys.stdin.readline().strip()
hand = sys.stdin.readline().strip()

# Solve the problem and print the result to stdout
result = solve(board, hand)
print(result)
