import sys

def min_balls_to_remove():
    # Read input from stdin
    board = input().strip()
    hand = input().strip()

    dp = [[0] * (len(board) + 1) for _ in range(6)]

    for i in range(len(board)):
        last_ball = ord(board[i]) - ord('R')
        for j in range(5, -1, -1):
            if j < len(board) and board[j] == board[i]:
                break
            dp[last_ball][i+1] = min(dp[last_ball][i] + 1, 
                                       dp[(last_ball + 3) % 6][j-1] if j > 0 else dp[last_ball][i])
        last_ball = (last_ball + 3) % 6

    # Check if all balls can be removed
    if dp[0][-1] == -1:
        return -1
    else:
        return dp[0][-1]

print(min_balls_to_remove())
