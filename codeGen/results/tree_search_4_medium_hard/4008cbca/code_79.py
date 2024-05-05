def min_insertions_to_remove_all_balls(board, hand):
    n = len(board)
    dp = [[float('inf')] * 6 for _ in range(n + 1)]
    dp[0][3] = 0

    for i in range(1, n + 1):
        prev_ball = board[i - 1]
        for j in range(4, -1, -1):
            if (j == 3 and prev_ball != 'R' and prev_ball != 'Y' and prev_ball != 'B' and prev_ball != 'G') or \
               (j == 2 and prev_ball != 'W'):
                dp[i][j] = min(dp[i][j], dp[i - 1][j])
            elif j in [0, 1]:
                if prev_ball == 'R':
                    dp[i][3] = min(dp[i][3], dp[i - 1][2] + 1)
                elif prev_ball == 'Y':
                    dp[i][4] = min(dp[i][4], dp[i - 1][3] + 1)
                elif prev_ball == 'B':
                    dp[i][5] = min(dp[i][5], dp[i - 1][4] + 1)
                else:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j])
            else:
                if prev_ball == 'R' and j in [3, 4]:
                    dp[i][3] = min(dp[i][3], dp[i - 2][2] + 1)
                elif prev_ball == 'Y' and j in [4, 5]:
                    dp[i][4] = min(dp[i][4], dp[i - 2][3] + 1)
                elif prev_ball == 'B' and j in [5, 0]:
                    dp[i][5] = min(dp[i][5], dp[i - 2][4] + 1)
                else:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j])

    if dp[n][3] != float('inf'):
        return len(hand) - 1
    elif dp[n][4] != float('inf'):
        return len(hand) - 2
    else:
        return -1

# Read the input from stdin
board = input()
hand = input()

print(min_insertions_to_remove_all_balls(board, hand))
