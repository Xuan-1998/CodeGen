python
import sys
from sys import stdin, stdout

n = int(stdin.readline())
a = [0] + list(map(int, stdin.readline().split()))
dp = [-1] * (n+1)
visited = [False] * (n+1)

def dfs(i):
    if i <= 0 or i > n:
        return 0
    if visited[i]:
        return -1
    if dp[i] != -1:
        return dp[i]
    visited[i] = True
    dp[i] = a[i] + dfs(i + a[i])
    if dp[i] >= 0:
        dp[i] += a[i]
    visited[i] = False
    return dp[i]

for i in range(1, n+1):
    stdout.write(str(dfs(i)) + "\n")

