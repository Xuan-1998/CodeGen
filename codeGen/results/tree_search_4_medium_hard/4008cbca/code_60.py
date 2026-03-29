def min_moves_to_remove_all_balls(board, hand):
    m = len(board)
    n = len(hand)
    dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]

    # Initialize the base case: we can't remove any balls if there are no balls on the board
    for j in range(n + 1):
        dp[0][j] = 0

    # Fill up the dp table
    for i in range(1, m + 1):
        for j in range(n + 1):
            prev_color = 'R' if i == 1 else board[i - 2]
            if prev_color == hand[j]:
                # If the current ball matches the previous ball's color, it can be removed along with the previous ball
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)
            elif j > 0:
                # If there are more than one balls in hand that match the current ball's color, then we can insert one of those balls and remove the current ball
                for k in range(j):
                    if hand[k] == prev_color:
                        dp[i][j] = min(dp[i][j], dp[i - 1][k] + 2)

    # Check if it is possible to remove all the balls by inserting some
    for j in range(n + 1):
        if dp[m][j] > 0:
            return dp[m][j]
    return -1

# Read input from stdin
board = input().strip()
hand = [input().strip() for _ in range(int(input()))]

# Print the result to stdout
print(min_moves_to_remove_all_balls(board, hand))
