def min_insertions(board):
    m = len(board)
    dp = [0] * (m + 1)

    for i in range(1, m + 1):
        if i < 3:
            A, B, C = board[:i]
            dp[i] = dp[i - 1] + 1
        else:
            prev_two_colors = set(board[i - 2:i])
            curr_color = board[i - 1]

            if len(prev_two_colors) == 1 and curr_color in prev_two_colors:
                A = True
                B = False
                C = False
            elif len(prev_two_colors) == 1:
                A = False
                B = True
                C = False
            else:
                A = False
                B = False
                C = True

            if A:
                dp[i] = dp[i - 1]
            elif B:
                dp[i] = dp[i - 1] + 1
            else:  # C
                for color in 'RGBW':
                    if (color != curr_color and board.count(color) >= 2):
                        dp[i] = min(dp[i], dp[i - 1] + 1)
                        break

    return dp[m]
