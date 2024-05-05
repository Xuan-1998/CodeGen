def min_operations_to_remove_balls(board, hand):
    # Initialize a dictionary to store the dynamic programming values
    dp = {i: float('inf') for i in range(len(board) + 1)}
    dp[0] = 0

    prev_removed = False

    for i in range(1, len(board) + 1):
        if board[i - 1] == hand[-1]:
            # If the current ball matches the color of the previous ball
            if not prev_removed:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[i], dp[i - 1] + (hand.count(hand[0]) or 2))
        else:
            # If the current ball does not match the color of the previous ball
            dp[i] = min(dp[i], dp[i - 1] + 1)
        prev_removed = board[i - 1] == hand[-1]

    if dp[-1] == float('inf'):
        return -1
    else:
        return dp[-1]
