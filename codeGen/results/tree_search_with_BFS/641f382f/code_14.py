import sys
from math import gcd

def solve():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))

    if 1 in a:
        return 0

    dp = [float('inf')] * n
    for i in range(n):
        g = a[i]
        for j in range(i, n):
            g = gcd(g, a[j])
            if g == 1:
                dp[j] = min(dp[j], dp[i-1] if i > 0 else 0) + j - i
    if dp[-1] == float('inf'):
        return -1
    return dp[-1] + n - 1

print(solve())

