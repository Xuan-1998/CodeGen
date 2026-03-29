import sys

n, m = map(int, input().split())
dp = [[False] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = True
        for k in range(i - 1, -1, -1):
            if not (dp[k][j] and all(x <= y for x, y in zip(subtable[k][j:], subtable[i-1][j:]))):
                dp[i][j] = False
                break

k = int(input())
for _ in range(k):
    l, r = map(int, input().split())
    print("Yes" if all(dp[r][j] for j in range(1, m + 1)) else "No")
