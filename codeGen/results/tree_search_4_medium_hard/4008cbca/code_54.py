import sys
from collections import defaultdict

# Read input from standard input
board = list(input())
hand = [c for c in input() if c in 'RBYGW']

dp = [[0] * 7 for _ in range(len(board) + 1)]
for i, prev_color in enumerate([(None, None)] + [(board[j - 1], board[j - 2]) for j in range(2, len(board) + 1)]):
    for j in range(7):
        if prev_color[0] is None:
            dp[i][j] = int(hand.count(chr(j + ord('R')))) if j == ord('R') else sys.maxsize
        elif chr(prev_color[0]) == chr(j + ord('R')):
            dp[i][j] = dp[i - 1][ord(prev_color[0])] + (int(hand.count(chr(j + ord('R'))))) // 3 * 2
        else:
            dp[i][j] = min(dp[i - 1][prev_color[0]] + int(hand.count(chr(j + ord('R')))) if j == ord('R') else sys.maxsize, dp[i - 1][ord(prev_color[0])] + (int(hand.count(chr(j + ord('R'))))) // 3 * 2) if chr(prev_color[0]) != chr(j + ord('R')) else dp[i - 1][prev_color[0]]

print(dp[-1][None] if any(c in 'RBYGW' for c in board) else -1)
