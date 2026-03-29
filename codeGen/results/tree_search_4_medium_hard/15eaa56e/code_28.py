import sys

n, m = map(int, input().split())
dp = [[True] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] > row[j - 1]:
            dp[i][j] = False
for _ in range(int(input())):
    l, r = map(int, input().split())
    found = False
    for c in range(m):
        if all(dp[i][c] for i in range(l, r + 1)):
            print("Yes")
            found = True
            break
    if not found:
        print("No")
