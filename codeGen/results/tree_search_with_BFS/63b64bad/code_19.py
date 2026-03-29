import sys
from sys import stdin, stdout
sys.setrecursionlimit(10**6)

def solve(i):
    if dp[i] != -2:
        return dp[i]
    dp[i] = -1
    visited[i] = True
    next = i + a[i]
    if next <= 0 or next > n:
        dp[i] = a[i]
    elif visited[next]:
        dp[i] = -1
    else:
        temp = solve(next)
        if temp == -1:
            dp[i] = -1
        else:
            dp[i] = temp + a[i]
    visited[i] = False
    return dp[i]

n = int(stdin.readline())
a = [0] + list(map(int, stdin.readline().split()))
dp = [-2] * (n+1)
visited = [False] * (n+1)
dp[1] = 0

for i in range(1, n+1):
    stdout.write(str(solve(i)) + "\n")

