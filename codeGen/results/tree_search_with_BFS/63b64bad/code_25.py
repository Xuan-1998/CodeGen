python
import sys
from sys import stdin, stdout

def dfs(x, a, dp, visited, stack):
    visited[x] = True
    stack[x] = True
    nx = x + a[x]
    ny = dp[x] + a[x]
    if nx > n or nx <= 0:
        dp[x] = ny
    elif stack[nx]:
        dp[x] = -1
    elif visited[nx]:
        dp[x] = ny + max(0, dp[nx])
    else:
        dp[x] = dfs(nx, a, dp, visited, stack)
        if dp[x] != -1:
            dp[x] += ny
    stack[x] = False
    return dp[x]

n = int(stdin.readline())
a = [0] + list(map(int, stdin.readline().split()))
dp = [-1]*(n+1)
visited = [False]*(n+1)
stack = [False]*(n+1)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i, a, dp, visited, stack)

for i in range(2, n+1):
    stdout.write(str(dp[i]) + '\n')

