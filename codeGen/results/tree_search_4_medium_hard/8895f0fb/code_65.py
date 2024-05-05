import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    dp = [0] * (N + 1)
    carry_prob = 1 / 10.0

    for i in range(1, N + 1):
        for j in range(min(i, 2), -1, -1):
            if j == 0:
                dp[i] += carry_prob
            else:
                dp[i] += dp[j - 1] * (10 ** (N - i))
                if j < i:
                    dp[i] += carry_prob

    expected_value = sum(dp) / (2 ** N)
    print(f"{expected_value:.6f}")
