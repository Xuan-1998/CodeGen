import sys

n = int(input())
a = list(map(int, input().split()))
dp = [[0]*106 for _ in range(n+1)]

for i in range(105):
    dp[0][i] = i
for i in range(1, n+1):
    for j in range(min(a[i-1], 104)+1):
        if a[i-1] == j:
            dp[i][j] = max(dp[i-1][max(j-1, 0)], dp[i-1][min(j+1, 104)])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(max(dp[n]))
