import sys

def min_insertions(board, hand):
    n = len(board)
    m = len(hand)
    
    # Initialize the result (minimum number of balls to insert)
    res = -1
    
    for i in range(n):
        # Check if we can remove all the balls by inserting from the hand
        removable = True
        for j in range(i, n):
            if board[j] == hand[0]:
                break
            elif len(set([board[k] for k in range(j, n)])) < 3:
                removable = False
                break
        
        if not removable:
            continue
        
        # Calculate the maximum number of balls that can be removed with this configuration
        max_removable = 0
        for j in range(i, n):
            if board[j] == hand[0]:
                max_removable += 1
            elif len(set([board[k] for k in range(j, n)])) < 3:
                break
        
        # If we can remove all the balls, update the result and increment the counter
        if max_removable >= n - i:
            res = min(res if res != -1 else m + 1, max_removable)
    
    return res

board = input().strip()
hand = input().strip()
print(min_insertions(board, hand))
