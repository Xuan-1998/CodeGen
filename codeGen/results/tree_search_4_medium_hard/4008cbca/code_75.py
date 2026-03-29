def min_moves_to_remove_all_balls():
    board = input().strip()
    hand = input().strip()

    dp = [[[float('inf')] * (len(hand) + 1) for _ in range(len(board) + 1)] for _ in range(2)]

    dp[0][0][0] = 0

    for i in range(1, len(board) + 1):
        for j in range(i):
            if board[j-1] == board[i-1]:
                dp[1][i][0] = min(dp[1][i][0], dp[0][j-1][0] + 1)
            else:
                dp[1][i][0] = dp[0][j-1][0]

        for k in range(1, len(hand) + 1):
            if i >= len(board) or board[i-1] != hand[k-1]:
                dp[1][i][k] = min(dp[1][i][k], dp[1][i-1][k-1] + 1)
            else:
                dp[1][i][k] = dp[0][i-1][k-1]

    return -1 if dp[1][-1][-1] == float('inf') else dp[1][-1][-1]
