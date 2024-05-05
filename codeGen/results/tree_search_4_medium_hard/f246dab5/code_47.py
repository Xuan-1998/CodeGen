import sys

n = int(input())
dp = [[0] * 4 for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][1] = min(dp[i-1][1], 20)  # cost of the first ticket
    for j in range(2, min(i+1, 3)):
        if i <= (j * 90 - 1):  # can use the jth ticket
            dp[i][j] = dp[i-(j*90-1)][j-1] + 50
        else:
            dp[i][j] = dp[i-1][j]

for _ in range(n):
    t = int(input())
    for j in range(3, -1, -1):
        if t <= (j * 1440 - 1):  # can use the jth ticket
            print(dp[t][j])
            break
