from collections import deque

def solve(board, hand):
    dp = {(b, 0): 0 for b in set(board)}  # base case: when board is empty
    last_ball = None
    for i, b in enumerate(board):
        if last_ball == (b, 1):  # consecutive same color balls
            dp[(b, i + 2)] = min(dp.get((b, i + 1), float('inf')) - 3, dp.get((b, i), float('inf')))
        else:
            dp[(b, i + 1)] = dp.get((last_ball, i), 0) if last_ball in hand else dp[(b, i)] + 1
        last_ball = (b, i)
    return -1 if dp.get(last_ball, float('inf')) > len(board) - 1 else min(dp.values())

# read input from stdin
board = input().strip()
hand = input().strip()

print(solve(board, hand))
