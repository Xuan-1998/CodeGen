import sys
from sys import stdin, stdout
from collections import defaultdict

def solve():
    n = int(stdin.readline())
    a = [0] + list(map(int, stdin.readline().split()))
    dp = [-2] * (n + 1)
    vis = [0] * (n + 1)
    for i in range(1, n + 1):
        if dp[i] != -2:
            continue
        stack = [i]
        vis[i] = 1
        while stack:
            v = stack[-1]
            if v + a[v] > n or v + a[v] < 1:
                dp[v] = a[v]
                stack.pop()
            elif dp[v + a[v]] != -2:
                dp[v] = dp[v + a[v]] + a[v]
                stack.pop()
            elif vis[v + a[v]]:
                dp[v] = -1
                stack.pop()
            else:
                stack.append(v + a[v])
                vis[v + a[v]] = 1
        while stack:
            v = stack[-1]
            if dp[v] != -1:
                dp[v] = dp[v + a[v]] + a[v]
            stack.pop()
    for i in range(1, n + 1):
        stdout.write(str(dp[i]) + "\n")

solve()

