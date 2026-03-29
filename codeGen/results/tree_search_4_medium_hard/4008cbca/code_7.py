import sys

def min_moves(board, hand):
    n = len(board)
    m = len(hand)
    dp = [0] * (n + m + 1)

    # Base case: when the board is empty, no moves are needed
    dp[0] = 0

    for i in range(1, n + 1):
        for j in range(m):
            if board[i - 1] == hand[j]:  # Insert a ball from the hand at this position
                dp[i + j] = min(dp[i + j], dp[i - 1] + 1)  # Update the DP table
            else:
                dp[i + j] = dp[i - 1]

    return dp[-1]

# Example usage:
board = input().strip()
hand = input().strip()
print(min_moves(board, hand))
