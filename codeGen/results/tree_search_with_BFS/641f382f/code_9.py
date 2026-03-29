import sys
import math

def solve():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))

    if 1 in a:
        return n - a.count(1)

    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    ans = float('inf')

    for i in range(n):
        dp[i][i] = a[i]
        for j in range(i+1, n):
            dp[i][j] = math.gcd(dp[i][j-1], a[j])
            if dp[i][j] == 1:
                ans = min(ans, j - i)

    if ans == float('inf'):
        return -1
    else:
        return ans + n - 1

print(solve())

