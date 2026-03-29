def min_moves_to_remove_all_balls():
    board, hand = [line.strip() for line in sys.stdin.readlines()]
    
    dp = {}
    prev_prev_color = None
    prev_color = None
    
    for i, ball in enumerate(board):
        if prev_prev_color == prev_color and prev_prev_color == ball:
            dp[i] = 0
        elif prev_prev_color is not None and prev_prev_color != ball:
            dp[i] = 1
        else:
            dp[i] = 0
        
        prev_prev_color, prev_color = prev_color, ball
    
    return max(dp.values(), default=-1)

print(min_moves_to_remove_all_balls())
