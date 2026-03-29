import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))
dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(i, n+1):
        if a[j-1] <= a[j]:
            dp[i][j] = dp[i-1][min(i,j)-1] + 1
        else:
            dp[i][j] = 1

for _ in range(m):
    l, r = map(int, input().split())
    print("Yes" if (a[r-1] <= a[r-2]) and (dp[l-1][r-1] >= 2) else "No")
