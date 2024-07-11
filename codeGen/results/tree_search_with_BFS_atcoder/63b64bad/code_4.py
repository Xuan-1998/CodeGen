import sys
from sys import stdin, stdout

def dfs(i, a, dp, visited, inStack):
    visited[i] = True
    inStack[i] = True

    nxt = i + a[i]
    if nxt <= n and not visited[nxt]:
        dp[i] = a[i] + dfs(nxt, a, dp, visited, inStack)
    elif nxt > n or inStack[nxt]:
        dp[i] = a[i]
    else:
        dp[i] = a[i] + dp[nxt]

    inStack[i] = False
    return dp[i]

n = int(stdin.readline().strip())
a = [0] + list(map(int, stdin.readline().strip().split()))
dp = [-1] * (n+1)
visited = [False] * (n+1)
inStack = [False] * (n+1)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i, a, dp, visited, inStack)

for i in range(1, n+1):
    stdout.write(str(dp[i]) + '\n')

