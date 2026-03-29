import sys
from sys import stdin, stdout

def dfs(i):
    if i <= 0 or i > n:
        return 0
    if visited[i]:
        if done[i]:
            return dp[i]
        else:
            return -1
    visited[i] = True
    dp[i] = dfs(i + 2*a[i]) if i % 2 == 1 else dfs(i - 2*a[i])
    if dp[i] == -1:
        return -1
    dp[i] += 2*a[i]
    done[i] = True
    return dp[i]

n = int(stdin.readline())
a = [0] + list(map(int, stdin.readline().split()))
dp = [0]*(n+1)
visited = [False]*(n+1)
done = [False]*(n+1)
for i in range(1, n+1):
    stdout.write(str(dfs(i)) + '\n')

