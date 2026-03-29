def min_balls_to_remove(input_board, input_hand):
    # Initialize the counter for the minimum number of balls needed
    min_balls = 0
    
    # Iterate through the "board" string and remove sets of three or more consecutive balls with the same color
    i = 0
    while i < len(input_board):
        count = 1
        current_color = input_board[i]
        for j in range(i + 1, len(input_board)):
            if input_board[j] == current_color:
                count += 1
            else:
                break
        if count >= 3:
            min_balls += 1
            i += (count - 2)
        else:
            i += 1
    
    # Insert balls from the "hand" string into the "board" string to fill gaps or create sets of three or more consecutive balls with the same color
    for ball in input_hand:
        while min_balls > 0 and len(input_board) < 20:  # check if board length is not exceeded
            if all(ball == c for c in input_board):  # check if ball is already on the board
                break
            if (len(input_board) % 5 != 0 or ball == 'W' or ball == 'B') and min_balls > 0:  # check if it's possible to insert a ball without exceeding the limit of consecutive same color balls
                input_board += ball
                min_balls -= 1
            else:
                break
    
    return -1 if len(input_board) > 20 else min_balls

import sys
board = input().strip()
hand = input().strip()
print(min_balls_to_remove(board, hand))
