import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(i):
        if a[j - 1] <= a[i - 1]:
            dp[i][j] = max(dp[i][j], dp[j][j] + (i - j))
        else:
            dp[i][j] = max(dp[i][j], dp[j][j])

for _ in range(m):
    l, r = map(int, input().split())
    print("Yes" if dp[r][l] == (r - l) else "No")
