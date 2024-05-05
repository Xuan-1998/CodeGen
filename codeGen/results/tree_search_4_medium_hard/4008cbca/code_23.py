import sys
from collections import defaultdict

def min_moves_to_remove_all_balls(board, hand):
    dp = [sys.maxsize] * (len(board) + 1)
    dp[0] = 0  # base case: no moves needed to remove all balls from an empty board

    for i in range(1, len(board) + 1):  # iterate through the board
        if board[i - 1] not in hand:  # check if we can insert a ball of the same color as the last one on the table
            dp[i] = min(dp[i], dp[i - 1] + 1)
        else:
            for c, count in defaultdict(int).fromkeys(hand, 0).items():
                if board[i - 1] == c:  # check if we can remove at least three balls with the same color
                    if count >= 3:
                        dp[i] = min(dp[i], dp[i - count])
                        break
            else:  # if we can't remove at least three balls with the same color, try inserting a ball
                for c in set(hand):
                    if board[i - 1] != c and (dp[i - 1] + 1) < dp[i]:
                        dp[i] = dp[i - 1] + 1

    return -1 if dp[-1] == sys.maxsize else dp[-1]

# read input from stdin
board = input().strip()
hand = input().strip()

print(min_moves_to_remove_all_balls(board, hand))
