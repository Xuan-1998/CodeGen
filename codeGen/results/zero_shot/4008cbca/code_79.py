from collections import Counter

def min_insertions(board, hand):
    # Sort both the board and hand by color
    sorted_board = sorted(Counter(board).items())
    sorted_hand = sorted(Counter(hand).items())

    inserted_count = 0
    
    while True:
        found_match = False
        
        for ball in sorted_board[:]:
            if ball[1] > 2:
                # If there are more than two of the same color, remove them
                sorted_board.remove(ball)
                found_match = True
                break
            
            for color, count in sorted_hand[:]:
                if color == ball[0] and count > 0:
                    # If there is a matching ball in hand, insert it
                    sorted_hand.remove((color, count - 1))
                    inserted_count += 1
                    found_match = True
                    break
            
            if found_match:
                break
        
        if not found_match:
            break
    
    return -1 if len(sorted_board) > 0 else inserted_count
