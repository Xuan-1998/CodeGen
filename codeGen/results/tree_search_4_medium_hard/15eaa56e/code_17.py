import sys

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

dp = [[True] * m for _ in range(n)]

for i in range(1, n):
    for j in range(m):
        if all(table[i][j] >= table[i - 1][j] for _ in range(j)):
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = False

for l, r in [tuple(map(int, input().split())) for _ in range(k)]:
    if all(all(table[k][j] >= table[k - 1][j] for j in range(m)) for k in range(l, r + 1)):
        print("Yes")
    else:
        print("No")
