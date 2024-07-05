python
import sys
from sys import stdin, stdout
sys.setrecursionlimit(10**6)

def dfs(i, a, dp, color):
    color[i] = 1
    next1 = i + a[i]
    next2 = i - a[i]
    if next1 <= n and color[next1] != 2:
        if color[next1] == 1 or (dp[next1] == -1 and dfs(next1, a, dp, color)):
            dp[i] = -1
            return True
        dp[i] = max(dp[i], dp[next1] + a[i])
    if next2 > 0 and color[next2] != 2:
        if color[next2] == 1 or (dp[next2] == -1 and dfs(next2, a, dp, color)):
            dp[i] = -1
            return True
        dp[i] = max(dp[i], dp[next2] + a[i])
    color[i] = 2
    return False

n = int(stdin.readline())
a = [0] + list(map(int, stdin.readline().split()))
dp = [-1] * (n + 1)
color = [0] * (n + 1)
dp[1] = 0
color[1] = 2
for i in range(2, n + 1):
    if dp[i] == -1:
        dfs(i, a, dp, color)
for i in range(2, n + 1):
    stdout.write(str(dp[i]) + '\n')

