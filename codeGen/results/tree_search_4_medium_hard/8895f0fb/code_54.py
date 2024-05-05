import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        min_carry = 9 - (i - 1) + dp[i - 1]
        max_carry = max(0, 10 - dp[i - 1] - 5)
        dp[i] = min(min_carry, max_carry)
    expected_carries = sum(dp[1:]) / N
    print(f"{expected_carries:.9f}")
