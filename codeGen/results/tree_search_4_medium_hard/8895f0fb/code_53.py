import sys

def expected_carries(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for msd in range(10):
            carry = max(0, 10 - msd - 5) if i > 1 else min(9 - i, max(0, 10 - msd - 5))
            dp[i] += carry
    return sum(dp[1:]) / (2 ** n)

T = int(input())
for _ in range(T):
    N = int(input())
    print(expected_carries(N))
