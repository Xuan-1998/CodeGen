import sys
from sys import stdin, stdout

def dfs(i, a, dp, vis):
    if vis[i] == 1:
        return -1
    if vis[i] == 2:
        return dp[i]
    vis[i] = 1
    dp[i] = dfs(i + a[i], a, dp, vis)
    if dp[i] != -1:
        dp[i] += a[i]
    vis[i] = 2
    return dp[i]

def solve():
    n = int(stdin.readline())
    a = [0] + list(map(int, stdin.readline().split())) + [0]
    dp = [-1] * (n+2)
    vis = [0] * (n+2)
    for i in range(1, n+1):
        if dp[i] == -1:
            dfs(i, a, dp, vis)
    for i in range(1, n+1):
        stdout.write(str(dp[i]) + '\n')

solve()

