def min_moves_to_remove_balls(board, hand):
    n = len(board)
    dp = [float('inf')] * (n + 1)  # Initialize dynamic programming table

    for i in range(1, n + 1):  # Iterate through the board from left to right
        if i >= 3 and board[i-3] == board[i-2] == board[i-1]:  # Three or more consecutive balls of same color
            dp[i] = min(dp[i], dp[i-3])
        else:
            dp[i] = dp[i-1]

    return dp[n-1] if dp[n-1] != float('inf') else -1

# Example usage:
board = input().strip()
hand = input().strip()

result = min_moves_to_remove_balls(board, hand)
print(result)
