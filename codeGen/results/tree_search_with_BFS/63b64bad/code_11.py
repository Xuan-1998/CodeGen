python
import sys
from sys import stdin, stdout
from collections import deque

n = int(stdin.readline())
a = [0] + list(map(int, stdin.readline().split()))
dp = [-1] * (n + 1)
visited = [False] * (n + 1)

def dfs(i):
    if i <= 0 or i > n:
        return 0
    if visited[i]:
        return -1
    visited[i] = True
    next1 = i + a[i]
    next2 = i - a[i]
    dp1 = dfs(next1)
    if dp1 != -1:
        dp1 += a[i]
    dp2 = dfs(next2)
    if dp2 != -1:
        dp2 += a[i]
    dp[i] = max(dp1, dp2)
    visited[i] = False
    return dp[i]

for i in range(2, n + 1):
    if dp[i] == -1:
        dp[i] = dfs(i)
    stdout.write(str(dp[i]) + '\n')

