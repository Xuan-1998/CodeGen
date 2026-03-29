import sys

def solve(board, hand):
    dp = [[-1 for _ in range(len(hand) + 1)] for _ in range(sum(1 for x in board) + 1)]

    def transition(i, j):
        if i == 0 and j == -1:  # initial state
            return 0
        if i > 0:
            for k, h in enumerate(hand):
                if h != board[j]:
                    dp[i][j] = min(dp[i-1][j], transition(i-1, (k+1)%len(hand)) + 1)
                    break
        return -1

    min_moves = sys.maxsize
    for i in range(sum(1 for x in board) + 1):
        if dp[i][-1] != -1:
            min_moves = min(min_moves, dp[i][-1])

    return -1 if min_moves == sys.maxsize else min_moves

board = input().strip()
hand = list(input().strip())

print(solve(board, hand))
