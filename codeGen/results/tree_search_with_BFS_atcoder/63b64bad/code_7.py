import sys
from collections import defaultdict

def solve(x, y):
    if x <= 0 or x > n:
        return y
    if dp[x] != -2:
        return dp[x]
    dp[x] = -1
    result = solve(x + a[x], y + a[x])
    if result != -1:
        dp[x] = result
    return dp[x]

n = int(sys.stdin.readline())
a = [0] + list(map(int, sys.stdin.readline().split()))
dp = [-2]*(n+1)
for i in range(1, n+1):
    print(solve(i, 0))

