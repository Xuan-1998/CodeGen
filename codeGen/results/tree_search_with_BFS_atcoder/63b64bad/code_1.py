import sys
from sys import stdin, stdout
from collections import defaultdict

def solve(i, a, dp, visited):
    if visited[i]:
        return -1
    if dp[i] != -1:
        return dp[i]
    visited[i] = True
    x = i + a[i]
    y = a[i]
    if x < 1 or x > n:
        dp[i] = y
    else:
        temp = solve(x, a, dp, visited)
        if temp == -1:
            dp[i] = -1
        else:
            dp[i] = y + temp
    visited[i] = False
    return dp[i]

n = int(stdin.readline())
a = [0] + list(map(int, stdin.readline().split()))
dp = [-1] * (n + 1)
visited = [False] * (n + 1)

for i in range(1, n + 1):
    stdout.write(str(solve(i, a, dp, visited)) + '\n')

