import sys

n = int(input())
colors = input()

dp = [[0 for _ in range(3)] for _ in range(n+1)]

dp[1][0], dp[1][1], dp[1][2] = 1, 1, 1

for i in range(2, n+1):
    for j in range(3):
        dp[i][j] = min(dp[i-1][k] + (1 if k != j else 0) for k in range(3))

ans = max([dp[n][i] for i in range(3)])

print(ans)

for i in range(n-1, -1, -1):
    for j in range(3):
        if dp[i+1][j] == ans:
            print('R' if j==0 else 'G' if j==1 else 'B', end='')
            break
