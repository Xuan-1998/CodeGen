n = int(input())
a = list(map(int, input().split()))
dp = [[0]*n for _ in range(n)]

for i in range(1, n):
    if i > 1:
        dp[i][i-2] = max(dp[i-1][i-3], 1+dp[i-2][i-3]) if (a[i] - a[i-1]) % 2 == 0 else dp[i-1][i-2]
    for j in range(i):
        if i > j:
            dp[i][j] = max(dp[i-1][k-1] + 1 for k in range(j+1, i+1) if a[k] == a[j] or a[k] == a[j]-1)
        else:
            dp[i][j] = dp[i-1][j]

print(max(dp[n-1]))
