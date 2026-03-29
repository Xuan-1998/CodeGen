import sys
input = sys.stdin.readline

n = int(input())
a = [int(x) for x in input().split()]
dp = [[[0]*1007 for _ in range(1007)] for _ in range(n+1)]

for i in range(n+1):
    dp[i][0][0] = 1
for i in range(1, n+1):
    for j in range(1, min(i+1, a[i]+1)):
        if not (i > j-1 or ((a[i]%j==0) and dp[i-1][j-1][j-1])):
            dp[i][j][j] = 0
        else:
            dp[i][j][j] = (dp[i][j][j]+dp[i-1][j-1][j-1]) % (10**9 + 7)
for i in range(1, n+1):
    for j in range(a[i]+1):
        if a[i]%j==0:
            dp[i][a[i]][j] = (dp[i][a[i]][j]+dp[i-1][a[i]-1][j-1]) % (10**9 + 7)
print(sum(dp[n][i][i] for i in range(1, a[n]+2)))
