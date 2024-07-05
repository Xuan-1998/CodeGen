python
import sys
from sys import stdin, stdout

def dfs(i):
    visited[i] = True
    x = i + a[i]
    y = a[i]
    if x <= 0 or x > n:
        dp[i] = y
    elif visited[x]:
        dp[i] = -1
    else:
        if dp[x] == -2:
            dfs(x)
        if dp[x] == -1:
            dp[i] = -1
        else:
            dp[i] = dp[x] + y
    visited[i] = False

n = int(stdin.readline())
a = [0] + list(map(int, stdin.readline().split()))
dp = [-2 for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(1, n+1):
    if dp[i] == -2:
        dfs(i)

for i in dp[1:]:
    stdout.write(str(i) + '\n')

