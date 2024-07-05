python
from sys import stdin, stdout, setrecursionlimit
setrecursionlimit(10**6)

n = int(stdin.readline())
a = [0] + list(map(int, stdin.readline().split()))
dp = [0]*(n+1)
vis = [0]*(n+1)

def dfs(i):
    vis[i] = 1
    if i + a[i] <= n and vis[i + a[i]] != 1:
        dp[i] = a[i] + dfs(i + a[i])
    elif i + a[i] > n:
        dp[i] = a[i]
    else:
        dp[i] = -1
    vis[i] = 2
    return dp[i]

for i in range(1, n+1):
    if vis[i] == 0:
        dfs(i)

for i in range(1, n+1):
    stdout.write(str(dp[i]) + '\n')

