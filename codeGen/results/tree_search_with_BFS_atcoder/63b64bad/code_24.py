import sys
from sys import stdin, stdout

def dfs(i):
    visited[i] = 1
    if a[i] + i > n or a[i] + i <= 0:
        dp[i] = a[i]
    else:
        if visited[a[i] + i] == 0:
            dp[i] = a[i] + dfs(a[i] + i)
        elif visited[a[i] + i] == 1:
            dp[i] = -1
        else:
            dp[i] = a[i] + dp[a[i] + i]
    visited[i] = 2
    return dp[i]

n = int(stdin.readline())
a = [0] + list(map(int, stdin.readline().split()))
dp = [0] * (n + 1)
visited = [0] * (n + 1)

for i in range(1, n + 1):
    if visited[i] == 0:
        dfs(i)

for i in range(1, n + 1):
    stdout.write(str(dp[i]) + "\n")

