import sys
from sys import stdin, stdout
sys.setrecursionlimit(10**6)

n = int(stdin.readline())
a = [0] + list(map(int, stdin.readline().split()))

dp = [-1] * (n+1)
visited = [False] * (n+1)

def dfs(x):
    if x <= 0 or x > n:
        return 0
    if dp[x] != -1:
        return dp[x]
    if visited[x]:
        return -1
    visited[x] = True
    y = dfs(x + a[x])
    visited[x] = False
    if y == -1:
        return -1
    dp[x] = y + 2 * a[x]
    return dp[x]

for i in range(1, n+1):
    stdout.write(str(dfs(i)) + "\n")

