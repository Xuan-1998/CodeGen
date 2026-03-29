import sys
from sys import stdin, stdout

def solve(i):
    if i <= 0 or i > n:
        return 0
    if visited[i]:
        if dp[i] == -1:
            cycle[i] = True
        return dp[i]
    if dp[i] != -1:
        return dp[i]
    visited[i] = True
    next = i + a[i]
    y = solve(next)
    if cycle[i] or y == -1:
        cycle[i] = True
        dp[i] = -1
    else:
        dp[i] = a[i] + y
    visited[i] = False
    return dp[i]

n = int(stdin.readline())
a = [0] + list(map(int, stdin.readline().split()))
dp = [-1] * (n + 1)
visited = [False] * (n + 1)
cycle = [False] * (n + 1)

for i in range(1, n + 1):
    if dp[i] == -1:
        solve(i)

for i in range(2, n + 1):
    stdout.write(str(dp[i]) + '\n')

