def min_balls(board, hand):
    # Count the colors
    r_board = board.count('R')
    y_board = board.count('Y')
    b_board = board.count('B')
    g_board = board.count('G')
    w_board = board.count('W')

    r_hand = hand.count('R')
    y_hand = hand.count('Y')
    b_hand = hand.count('B')
    g_hand = hand.count('G')
    w_hand = hand.count('W')

    # Determine if it's possible to remove all balls
    if max([r_board, y_board, b_board, g_board, w_board]) >= 3:
        return -1

    # Calculate the minimum number of balls needed
    min_balls = sum([max([r_board // 3, r_hand]), 
                     max([y_board // 3, y_hand]), 
                     max([b_board // 3, b_hand]), 
                     max([g_board // 3, g_hand]), 
                     max([w_board // 3, w_hand])])

    return min_balls
