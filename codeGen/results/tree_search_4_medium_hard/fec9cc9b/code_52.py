import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][i] = (a[i-1] >= a[0])  # Base case: Initialize dp[1][n] to 1 if array is non-increasing and 0 otherwise
    for j in range(i-1, -1, -1):
        if a[j] >= a[j+1]:
            dp[i][j] = (dp[j+1][i-1]) | ((a[i-1] >= a[j]) & (dp[j][j]))
        else:
            break

for _ in range(m):
    l, r = map(int, input().split())
    if dp[r][r] & (dp[l-1][r]):
        print("Yes")
    else:
        print("No")
