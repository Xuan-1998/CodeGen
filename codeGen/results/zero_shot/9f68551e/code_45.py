import sys

def solve():
    n = int(sys.stdin.readline())
    k = list(map(int, sys.stdin.readline().split()))
    h = list(map(int, sys.stdin.readline().split()))

    dp = [0] * (n + 1)
    x = 1
    for i in range(1, n + 1):
        if x == 1:
            dp[i] = max(h[i - 1], x + 1)
        else:
            dp[i] = min(x + 1, h[i - 1]) + x
        x += 1

    return dp[n]

print(solve())
