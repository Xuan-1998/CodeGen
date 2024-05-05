import sys

def solve():
    n = int(input())
    board = input().strip()
    m = int(input())
    hand = input().strip()

    dp = [[-1] * (m + 1) for _ in range(n + 1)]

    dp[0][0] = 0
    for i in range(1, n + 1):
        if board[i - 1] == board[i - 2]:
            dp[i][0] = dp[i - 1][0]
        else:
            dp[i][0] = dp[i - 1][0] + 1

    for j in range(1, m + 1):
        if hand[j - 1] == board[0]:
            dp[0][j] = dp[0][j - 1]
        else:
            dp[0][j] = dp[0][j - 1] + 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if board[i - 1] == hand[j - 1]:
                if i > 1 and board[i - 2] == hand[j - 1]:
                    dp[i][j] = min(dp[i][j], dp[i - 2][j - 1])
                else:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1], dp[i][j - 1]) + (board[i - 1] != board[0])
            else:
                if i > 1 and board[i - 2] == board[i - 3]:
                    dp[i][j] = min(dp[i][j], dp[i - 2][j])
                elif j > 1 and hand[j - 2] == hand[j - 3]:
                    dp[i][j] = min(dp[i][j], dp[i][j - 2])
                else:
                    dp[i][j] = dp[i - 1][j] + 1

    print(-1 if dp[n][m] == -1 else dp[n][m])

if __name__ == "__main__":
    solve()
