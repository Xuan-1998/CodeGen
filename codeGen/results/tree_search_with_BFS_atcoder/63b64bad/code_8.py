import sys
from sys import stdin, stdout

def solve(i):
    if i <= 0 or i > n:
        return 0
    if dp[i] != -2:
        return dp[i]
    dp[i] = -1
    next = solve(i + a[i]) + a[i]
    if next == -1:
        return -1
    dp[i] = next
    return next

n = int(stdin.readline())
a = [0] + list(map(int, stdin.readline().split()))
dp = [-2]*(n+1)

for i in range(1, n+1):
    solve(i)

for i in range(1, n+1):
    stdout.write(str(dp[i]) + '\n')

