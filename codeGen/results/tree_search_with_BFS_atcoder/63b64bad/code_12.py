import sys
from sys import stdin, stdout

def dfs(x):
    visited[x] = True
    next_x = x + a[x]
    if next_x > n or next_x <= 0:
        dp[x] = a[x]
    elif dp[next_x] != -1:
        dp[x] = a[x] + dp[next_x]
    elif visited[next_x]:
        dp[x] = -1
    else:
        dp[x] = a[x] + dfs(next_x)
    visited[x] = False
    return dp[x]

n = int(stdin.readline())
a = [0] + list(map(int, stdin.readline().split()))
dp = [-1] * (n + 1)
visited = [False] * (n + 1)

for i in range(1, n + 1):
    if dp[i] == -1:
        dfs(i)

for i in range(2, n + 1):
    stdout.write(str(dp[i]) + "\n")

