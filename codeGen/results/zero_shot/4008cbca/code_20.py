def min_insertions(board, hand):
    # Initialize the count of inserted balls
    inserted = 0
    
    # Iterate through the board
    i = 0
    while i < len(board):
        # Check if there are three or more consecutive balls with the same color
        same_color = True
        j = i
        while j < len(board) and (board[j] == board[i]):
            j += 1
            if j - i >= 3:
                break
        if j - i < 3:
            same_color = False
        
        # If there are three or more consecutive balls with the same color, remove them
        if same_color:
            inserted += (j - i) // 3 * 3
            i = j
        else:
            # Insert one ball from our hand to break the chain
            inserted += 1
            board.insert(i, hand[0])
            hand = hand[1:]
    
    # If there are still balls left in our hand, it's not possible to remove all the balls
    if len(hand) > 0:
        return -1
    
    return inserted

# Read input from stdin
board = input().strip()
hand = [input().strip() for _ in range(int(input()))]

# Calculate and print the result
print(min_insertions(board, hand))
