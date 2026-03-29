def min_moves_to_remove_all_balls(board, hand):
    dp = {}
    max_len = len(hand)
    
    for i in range(max_len + 1):
        if i == 0:
            dp[board] = 0
        else:
            last_ball_color = board[-1]
            
            # consider each possible move (inserting a new ball)
            for color in hand:
                new_board = board[:-1] + color
                
                # update the dynamic programming table with the minimum number of moves needed to remove all balls given this last ball
                if new_board not in dp:
                    dp[new_board] = min_moves_to_remove_all_balls(new_board, hand) + 1
                else:
                    dp[new_board] = dp[board[-1]] + 1
            
            # update the dynamic programming table with the minimum number of moves needed to remove all balls given this last ball
            if board not in dp:
                dp[board] = float('inf')
            else:
                dp[board] = dp[board]
    
    return dp.get(board, -1)

# test your function
board = input().strip()
hand = input().strip()
print(min_moves_to_remove_all_balls(board, hand))
