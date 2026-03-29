def min_moves_to_remove_all_balls(board):
    n = len(board)
    
    # Initialize dynamic programming table
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        if board[i - 1] == '-':  # If there's no ball at the current position
            dp[i] = min(dp[i], dp[i - 1])
        else:
            # Try to remove all balls up to this point
            removed_at_i = float('inf')
            for j in range(i, n + 1):
                if board[j - 1] == board[i - 1]:  # If the current ball is the same color as the one at i - 1
                    removed_at_i = min(removed_at_i, dp[j - 1])
                    break
            
            if removed_at_i != float('inf'):
                dp[i] = min(dp[i], removed_at_i + (i - j) if board[j - 1] == '-' else 0)
    
    return dp[-1] if dp[-1] < float('inf') else -1

# Read input from standard input
board = input().strip()
hand = input().strip()

print(min_moves_to_remove_all_balls(board))
