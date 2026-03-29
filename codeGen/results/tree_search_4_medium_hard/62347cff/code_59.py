n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
for i in range(n):
    dp[i][0] = m[i][0]
for j in range(n):
    dp[0][j] = m[0][j]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = m[i][j] + min(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
