import sys

def solve():
    n, t = map(int, input().split())
    fraction = float(input())

    dp = [0] * (n + 1)
    for i in range(n):
        digit = int((10 ** i) * fraction) % 10
        next_dp = max(dp[i], round(digit / (10 ** i)) + dp[max(0, i - 1)])
        dp[i + 1] = min(next_dp, t)

    return str(max(int(fraction * (10 ** n)), dp[-1]))

print(solve())
