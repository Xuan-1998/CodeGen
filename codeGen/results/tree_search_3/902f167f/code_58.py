import sys

n, m = map(int, input().split())
dp = [[float('inf')] * (m+1) for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = 1
for j in range(m+1):
    dp[0][j] = 1

for i in range(1, n+1):
    for j in range(1, m+1):
        for k in range(i+1):
            if (k*k) <= (i*j):
                dp[i][j] = min(dp[i][j], dp[k][int((j+k)/2.0)] + 1)
            else:
                break

print(min(dp[n][m]))
