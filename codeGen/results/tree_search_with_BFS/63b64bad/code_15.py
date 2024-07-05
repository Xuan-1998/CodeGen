python
import sys
from sys import stdin, stdout

n = int(stdin.readline())
a = [0] + list(map(int, stdin.readline().split()))

dp = [-1] * (n+1)
visited = [0] * (n+1)

def solve(x):
    if x <= 0 or x > n:
        return 0
    if visited[x] == 1:
        return -1
    if dp[x] != -1:
        return dp[x]
    visited[x] = 1
    next_x = x + a[x] if x % 2 == 1 else x - a[x]
    dp[x] = solve(next_x) + a[x] if solve(next_x) != -1 else -1
    visited[x] = 2
    return dp[x]

for i in range(2, n+1):
    dp[i] = solve(i)
    stdout.write(str(dp[i]) + "\n")

