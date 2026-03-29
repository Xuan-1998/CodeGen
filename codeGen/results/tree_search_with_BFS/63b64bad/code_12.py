import sys
from sys import stdin, stdout
sys.setrecursionlimit(10**6)

n = int(stdin.readline())
a = [0] + list(map(int, stdin.readline().split()))
dp = [-2]*(n+1)
visited = [False]*(n+1)

def dfs(i, y):
    if i <= 0 or i > n: return y
    if visited[i]: return -1
    visited[i] = True
    dp[i] = dfs(i+a[i], y+a[i])
    if dp[i] != -1: dp[i] = max(dp[i], dfs(i-a[i], y+a[i]))
    visited[i] = False
    return dp[i]

for i in range(1, n+1):
    if dp[i] == -2: dp[i] = dfs(i, 0)

for i in dp[1:]:
    stdout.write(str(i) + '\n')

