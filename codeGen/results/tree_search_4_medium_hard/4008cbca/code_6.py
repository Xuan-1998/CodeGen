def min_moves_to_remove_balls(board, hand):
    m, n = len(board), len(hand)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        last_removed_color = board[i - 1]
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = 0
            elif j == 0:
                dp[i][j] = float('inf')
            else:
                min_moves = float('inf')
                for k in range(i - 1, -1, -1):
                    if board[k] != last_removed_color and hand[j - 1] == board[k]:
                        min_moves = min(min_moves, dp[k][j - 1] + 1)
                dp[i][j] = min(dp[i - 1][j], min_moves)

    return -1 if dp[m][n] == float('inf') else dp[m][n]

board = input().strip()
hand = input().strip()

print(min_moves_to_remove_balls(board, hand))
