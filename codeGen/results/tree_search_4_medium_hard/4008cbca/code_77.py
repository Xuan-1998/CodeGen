def min_insertions(board, hand):
    n = len(board)
    dp = [[0] * (len(hand) + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(len(hand) + 1):
            if j == 0:
                dp[i][j] = i
            else:
                dp[i][j] = min(dp[i - 1][k] + (board[i - 1] != hand[k]) for k in range(j)) + 1
    
    return dp[-1][-1]
