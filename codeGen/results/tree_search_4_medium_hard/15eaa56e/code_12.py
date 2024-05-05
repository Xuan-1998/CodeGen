import sys

n, m = map(int, input().split())
dp = [[False] * m for _ in range(n)]

for i in range(1, n):
    for j in range(m):
        prev_max = -sys.maxsize
        for k in range(i):
            if table[k][j] <= table[i-1][j]:
                prev_max = table[k][j]
                break
        dp[i][j] = True if prev_max != -sys.maxsize else False

for task in [list(map(int, input().split())) for _ in range(k)]:
    l, r = task[0], task[1]
    print("Yes" if any(dp[row][col] for row in range(l-1, r+1) for col in range(m)) else "No")
