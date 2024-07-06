import sys
from sys import stdin, stdout
sys.setrecursionlimit(10**6)

def dfs(i):
    visited[i] = 1
    next_i = i + a[i]
    if next_i <= n and visited[next_i] != 2:
        if visited[next_i] == 1:
            dp[i] = -1
        else:
            dp[i] = a[i] + (dp[next_i] if dfs(next_i) else 0)
    else:
        dp[i] = a[i]
    visited[i] = 2
    return dp[i] != -1

n = int(stdin.readline())
a = [0] + list(map(int, stdin.readline().split()))
dp = [-2]*(n+1)
visited = [0]*(n+1)

for i in range(1, n+1):
    if visited[i] == 0:
        dfs(i)

for i in range(1, n+1):
    stdout.write(str(dp[i]) + '\n')

