import sys

n, m = map(int, input().split())
array = list(map(int, input().split()))
dp = [[False] * n for _ in range(n)]
for i in range(1, n):
    if array[i - 1] <= array[i]:
        dp[i][i] = True
    else:
        dp[i][i] = False

for i in range(n - 2, -1, -1):
    for j in range(i + 1, n):
        if array[i] >= array[j]:
            dp[i][j] = dp[i][j - 1]
        else:
            dp[i][j] = max(dp[i][k] and dp[k + 1][j] for k in range(i, j))

for _ in range(m):
    l, r = map(int, input().split())
    if dp[l - 1][r - 1]:
        print("Yes")
    else:
        print("No")
