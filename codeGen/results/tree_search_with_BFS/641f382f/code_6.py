import math
from sys import stdin

def solve():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    if 1 in a:
        return n - a.count(1)
    dp = [0]*n
    for i in range(n):
        dp[i] = a[i]
        for j in range(i):
            dp[j] = math.gcd(dp[j], a[i])
            if dp[j] == 1:
                return n + i - j - 1
    return -1

print(solve())

