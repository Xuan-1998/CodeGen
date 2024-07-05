python
import sys
from sys import stdin, stdout

def dfs(i):
    visited[i] = 1
    next_i = i + a[i] if i % 2 == 1 else i - a[i]
    if next_i <= 0 or next_i > n:
        dp[i] = a[i]
    elif visited[next_i] == 1:
        dp[i] = -1
    elif visited[next_i] == 2:
        dp[i] = a[i] + dp[next_i]
    else:
        dfs(next_i)
        if dp[next_i] == -1:
            dp[i] = -1
        else:
            dp[i] = a[i] + dp[next_i]
    visited[i] = 2

n = int(stdin.readline())
a = [0] + list(map(int, stdin.readline().split()))
dp = [0] * (n + 1)
visited = [0] * (n + 1)

for i in range(2, n + 1):
    if visited[i] == 0:
        dfs(i)

for i in range(2, n + 1):
    stdout.write(str(dp[i]) + "\n")

