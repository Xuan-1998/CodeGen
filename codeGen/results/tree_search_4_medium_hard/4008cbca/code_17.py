def min_moves_to_remove_all_balls():
    board = input().strip()
    hand = input().strip()

    dp = [[float('inf')] * (len(hand) + 1) for _ in range(len(board) + 1)]
    last_color_seen_board = None
    last_color_seen_hand = None

    for i in range(1, len(board) + 1):
        for j in range(1, min(i+1, len(hand) + 1)):
            if board[i-1] == hand[j-1]:
                last_color_seen_board = last_color_seen_hand = board[i-1]
            else:
                last_color_seen_board = board[i-1] if i > 0 else None
                last_color_seen_hand = hand[j-1] if j > 0 else None

            for k in range(j):
                if (last_color_seen_board == hand[k] and
                        board[i-1] != hand[k]):
                    dp[i][j] = min(dp[i][j], dp[i-1][k])
                    break
            else:
                dp[i][j] = dp[i-1][j]

    if dp[-1][-1] == float('inf'):
        return -1
    else:
        return dp[-1][-1]
