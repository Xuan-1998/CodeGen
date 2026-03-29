import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(i, n + 1):
        if arr[j - 1] >= arr[i - 1]:
            dp[i][j] = dp[i-1][j-1] + arr[j-1]
        else:
            dp[i][j] = dp[i-1][j]

for _ in range(m):
    l, r = map(int, input().split())
    if dp[l - 1][r] == dp[r][r]:
        print('Yes')
    else:
        print('No')

