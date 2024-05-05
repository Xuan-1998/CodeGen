import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(2, n + 1):
    for j in range(i, n + 1):
        if a[i - 1] <= a[i]:
            dp[i][j] = max(dp[i - 1][k] for k in range(j) if a[k] <= a[k]) + 1
        else:
            dp[i][j] = max(dp[i - 1][k] for k in range(i, j + 1) if a[k] >= a[k]) + 1

for _ in range(m):
    l, r = map(int, input().split())
    print("Yes" if (dp[r][r] % 2 == 0) else "No")
