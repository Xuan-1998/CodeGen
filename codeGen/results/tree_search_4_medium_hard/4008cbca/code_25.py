from collections import defaultdict

def min_moves_to_remove_all_boards(board, hand):
    # Base case: When the board is empty, the minimum number of moves needed to remove all balls is 0.
    dp = {ball: 0 for ball in set(board)}
    
    for _ in range(len(hand)):
        last_ball_on_board = ''
        min_moves = float('inf')
        
        for ball in hand:
            if ball not in board:
                new_last_ball_on_board = ball
                moves = dp.get(new_last_ball_on_board, float('inf')) + 1
                
                # Update the minimum number of moves needed to remove all balls given this new last ball
                min_moves = min(min_moves, moves)
                
                last_ball_on_board = new_last_ball_on_board
        
        if min_moves == float('inf'):
            return -1
        
        dp[last_ball_on_board] = min_moves
    
    return min_moves

# Example usage:
board = input()
hand = input()

print(min_moves_to_remove_all_boards(board, hand))
