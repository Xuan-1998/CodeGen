def min_insertions(board, hand):
    # Initialize the count of remaining balls
    remaining = list(board)
    
    # Iterate over the balls in hand
    for ball in hand:
        # Add the current ball to the end of the board
        remaining.append(ball)
        
        # While there are three or more consecutive balls with the same color, remove them
        i = 0
        while i < len(remaining) - 2:
            if remaining[i] == remaining[i+1] == remaining[i+2]:
                remaining = remaining[:i] + remaining[i+3:]
            else:
                i += 1
        
        # If all balls are removed, return 0
        if not remaining:
            return 0
    
    # Calculate the minimum number of insertions needed
    min_inserts = len(hand)
    for i in range(len(board)):
        # Try inserting a ball at each position
        temp_board = list(board[:i]) + [hand[0]] + board[i:]
        j = 0
        while j < len(temp_board) - 2:
            if temp_board[j] == temp_board[j+1] == temp_board[j+2]:
                break
        else:
            remaining = temp_board
            i += 1
        # If all balls are removed, return the number of insertions needed
        if not remaining:
            return min_inserts + len(hand) - i
    
    # If it's not possible to remove all the balls, output -1
    return -1

# Example usage
board = input()
hand = input()
print(min_insertions(board, hand))
