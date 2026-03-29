def can_remove_all_balls(board, hand):
    # Check if it's possible to remove all balls
    for i in range(len(board) - 2):
        if board[i] == board[i+1] == board[i+2]:
            return True
    return False

def min_inserted_balls(board, hand):
    inserted = 0
    while can_remove_all_balls(board, hand):
        # Find groups of three or more consecutive balls with the same color
        for i in range(len(board) - 2):
            if board[i] == board[i+1] == board[i+2]:
                # Insert a ball of opposite color to break the group
                if hand.count(board[i]) > 0:
                    hand.remove(board[i])
                    inserted += 1
                # Remove the group of matching balls
                board = board[:i] + ['R', 'Y', 'B', 'G', 'W'] * (len(board) - i - 3)
                break
    return inserted

# Read input from stdin
board = input().strip()
hand = input().strip()

# Call the function to get the minimum number of inserted balls
min_inserted = min_inserted_balls(list(board), list(hand))

print(min_inserted if can_remove_all_balls(board, hand) else -1)
