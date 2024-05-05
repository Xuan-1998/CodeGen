def minMoves(board, hand):
    dp = [float('inf')] * (len(board) + 1)
    dp[0] = 0

    for i in range(len(board)):
        if board[i] == 'R':
            # Add a red ball to the board
            dp[i + 1] = min(dp[i], dp[i - 1] + 3) if i > 0 else dp[i]
        elif board[i] == 'Y':
            # Add a yellow ball to the board
            dp[i + 1] = min(dp[i], dp[i - 1] + 3) if i > 0 else dp[i]
        elif board[i] == 'B':
            # Add a blue ball to the board
            dp[i + 1] = min(dp[i], dp[i - 1] + 3) if i > 0 else dp[i]
        elif board[i] == 'G':
            # Add a green ball to the board
            dp[i + 1] = min(dp[i], dp[i - 1] + 3) if i > 0 else dp[i]
        elif board[i] == 'W':
            # Add a white ball to the board
            dp[i + 1] = min(dp[i], dp[i - 1] + 3) if i > 0 else dp[i]

    return dp[-1]

# Test cases
board = input()
hand = input()

print(minMoves(board, hand))
