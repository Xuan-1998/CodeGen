def minMovesToRemoveAllBalls(board, hand):
    dp = [[float('inf')] * (len(hand) + 1) for _ in range(len(board) + 1)]
    
    # Base case: empty board and no balls to use
    dp[0][0] = 0
    
    for i in range(1, len(board) + 1):
        for j in range(max(0, i - 3), len(hand) + 1):
            if board[i - 1] == hand[j - 1]:
                # If the top ball on the board matches the current hand ball,
                # remove it and try to use the remaining balls
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
            else:
                # If the top ball on the board doesn't match, consider three options:
                # 1. Insert a ball from the hand into the board.
                # 2. Remove a ball that is already in the board, if possible.
                # 3. Do nothing (stuck with the current state).
                dp[i][j] = min(dp[i - 1][j] + 1, dp[max(0, i - 3)][j] + 1, dp[i][j])
    
    return dp[-1][-1] if dp[-1][-1] != float('inf') else -1

board = input()
hand = input()

print(minMovesToRemoveAllBalls(board, hand))
