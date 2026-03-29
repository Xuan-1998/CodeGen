import sys

dp = [[0] * (2*10**5+7) for _ in range(20)]

for i in range(1, 20):
    dp[i][0] = 1
    for j in range(1, 2*10**5+7):
        if i == 0:
            dp[0][j] = 1
        elif i > 0 and j > 0:
            if i % 2 == 0:
                dp[i][j] = (dp[i//2][j-1] + dp[i//2][j]) % (10**9+7)
            else:
                dp[i][j] = ((dp[(i+1)//10][j-1] + dp[(i+1)//10][j]) * 10 + (i+1) % 10) % (10**9+7)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(dp[n][m])
