import sys

def min_insertions(board):
    n = len(board)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if i < 3:
            dp[i] = 0
        else:
            one, two, three = 0, 0, 0
            for j in range(i-1, -1, -1):
                if board[j] == 'R': one += 1
                elif board[j] == 'Y': two += 1
                elif board[j] == 'B': three += 1
                if (one >= 3 or two >= 3 or three >= 3) and j >= i-2:
                    dp[i] = min(dp[i], dp[j] + 1)
                    break
            else:
                dp[i] = dp[i-1]

    return -1 if dp[n] == n else dp[n]

board = input().strip()
hand = input().strip()

print(min_insertions(board))
