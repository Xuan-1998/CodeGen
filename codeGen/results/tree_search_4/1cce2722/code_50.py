from collections import deque

n = int(input())
a = list(map(int, input().split()))

dp = [[0] * (105) for _ in range(105)]
dp[1][2] = 1

for i in range(3, n+1):
    dp[i][i-2] = 1
    for j in range(i-4, -1, -1):
        dp[i][j] = max(dp[i][j], dp[i-1][j+1] + (a[i] != a[j+1]))

ans = 0
for i in range(1, n+1):
    ans = max(ans, dp[n][i])

print(ans)
