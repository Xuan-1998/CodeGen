import sys

def solve():
    n, x = map(int, input().split())
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        if len(str(x)) >= i:
            dp[i] = 0
            break
        for y in range(10):
            new_x = x * 10 + y
            operations = dp[i - 1 - len(str(new_x))]
            dp[i] = min(dp[i], operations + (i != n))

    if dp[n] == float('inf'):
        return -1
    else:
        return dp[n]

print(solve())
