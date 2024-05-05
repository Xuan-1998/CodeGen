from collections import defaultdict

board = input().strip()
hand = list(input().strip())

dp = [[0] * (len(hand) + 1) for _ in range(len(board) + 1)]
last_color = None
for i in range(1, len(board) + 1):
    dp[i][0] = i
    for j in range(1, len(hand) + 1):
        if board[:i][-1] == hand[-1]:
            if board[:i][-1] == last_color:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + (board[:i][-1] != board[:i][-2])
            else:
                dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j]
        last_color = hand[-1]

if dp[-1][-1] == 0:
    print(-1)
else:
    print(dp[-1][-1])
