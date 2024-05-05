def min_moves_to_remove_balls():
    dp = [[float('inf')] * 5 for _ in range(25)]
    dp[0][0] = 0

    for i in range(1, len(dp)):
        for j in range(5):
            if i < board_length:
                for k in range(5):
                    if (j == k and last_ball == 'R' or j == k and last_ball == 'Y' or 
                        j == k and last_ball == 'B' or j == k and last_ball == 'G'):
                        dp[i][j] = min(dp[i-1][k], dp[i-1][j]) + 1
            else:
                for k in range(5):
                    if j != k:
                        dp[i][j] = min(dp[i-1][k], dp[i-1][j]) + 1

    return dp[board_length][0]

# Receive inputs from stdin and print your answer to stdout.
board_length, last_ball = map(int, input().split())
print(min_moves_to_remove_balls())

