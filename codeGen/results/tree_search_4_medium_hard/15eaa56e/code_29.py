import sys

n, m = map(int, input().split())
dp = [[False] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, min(i, m) + 1):
        if all(row[k] <= row[k+1] for k in range(j-1, i)):
            dp[i][j] = True

k = int(input())
for _ in range(k):
    l, r = map(int, input().split())
    print("Yes" if any(dp[r][m]) else "No")
