def min_moves_to_remove_all_balls(board, hand):
    n = len(board)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # base case: when the board is empty

    for i in range(1, n + 1):
        if board[i - 1] in hand:
            dp[i] = min(dp[i], dp[i - 1])  # don't move
        else:
            for j in range(i):
                if board[j] == board[i - 1]:
                    break
            dp[i] = min(dp[i], dp[j - 1] + (i - j) * (3 - len(set(board[j:i]))))  # insert a ball

    return dp[-1] if dp[-1] != float('inf') else -1
