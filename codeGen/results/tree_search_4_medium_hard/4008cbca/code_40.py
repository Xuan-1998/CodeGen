import sys

dp = {}

def dp(board):
    if board in dp:
        return dp[board]
    n = len(board)
    res = float('inf')
    for i in range(n):
        if board[i] == 'R' or board[i] == 'Y' or board[i] == 'B' or board[i] == 'G':
            for j in range(i+3, n):
                if board[j] == board[i]:
                    res = min(res, 1 + dp(board[:i] + 'W' * (j - i)) + dp(board[j:] + hand))
    dp[board] = res
    return res

while True:
    try:
        board = input()
        hand = input()
        print(dp(board))
    except EOFError:
        break
