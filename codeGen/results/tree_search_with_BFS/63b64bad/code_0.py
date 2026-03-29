import sys
from sys import stdin, stdout

def dfs(i):
    if dp[i] != -2:
        return dp[i]
    if visited[i]:
        return -1
    visited[i] = True
    dp[i] = -1
    if i+a[i] <= n:
        temp = dfs(i+a[i])
        if temp == -1:
            return -1
        dp[i] = temp + a[i]
    visited[i] = False
    return dp[i]

n = int(stdin.readline())
a = [0] + list(map(int, stdin.readline().split()))
dp = [-2]*(n+1)
visited = [False]*(n+1)

for i in range(1, n+1):
    dfs(i)

for i in range(2, n+1):
    stdout.write(str(dp[i]) + '\n')

