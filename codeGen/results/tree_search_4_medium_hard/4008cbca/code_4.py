import sys

# Input: board and hand strings
board = input().strip()
hand = input().strip()

n = len(board)
m = len(hand)

dp = [0] * (n + 1)  # Initialize DP table with base case

for i in range(1, n + 1):
    if not hand:  # No balls in hand
        dp[i] = dp[i-1]
    else:
        # Consider inserting a ball at the current position
        dp[i] = min(dp[i-1], dp[i-1] + 1 + min(j for j in range(m) if board[i-1-j] == hand[j]))

# Output: minimum number of moves needed to remove all balls
print(dp[-1])
