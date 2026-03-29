import sys
from sys import stdin, stdout
sys.setrecursionlimit(10**6)

def dfs(x):
    if x <= 0 or x > n:
        return 0
    if visited[x]:
        return -1
    if dp[x] != -1:
        return dp[x]
    visited[x] = 1
    dp[x] = dfs(x + a[x]) + a[x]
    if dp[x] < 0:
        dp[x] = -1
    visited[x] = 0
    return dp[x]

n = int(stdin.readline())
a = [0] + list(map(int, stdin.readline().split()))
dp = [-1] * (n+1)
visited = [0] * (n+1)

for i in range(1, n+1):
    stdout.write(str(dfs(i)) + '\n')

