import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[1] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(i):
        if arr[j] <= arr[i]:
            dp[i][j] = max(dp[i][j], dp[j][j] + 1)

for _ in range(m):
    l, r = map(int, input().split())
    print('Yes' if dp[r][r] - dp[l-1][l-1] >= 0 else 'No')
