import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][i] = 1
    for j in range(i - 1, -1, -1):
        if arr[j] >= arr[i]:
            dp[j][i] = max(dp[j][i], dp[j][i - 1] + 1)
        else:
            dp[j][i] = 0

for _ in range(m):
    l, r = map(int, input().split())
    if any(dp[l - 1][i] > 0 for i in range(l, r + 1)):
        print("Yes")
    else:
        print("No")
