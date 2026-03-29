import sys

def solve():
    n, m, h = map(int, input().split())
    dp = [0.0] * (n + 1)
    dp[0] = 1.0  # base case: one team with zero players is possible

    for i in range(1, n + 1):
        dp[i] = sum(dp[j] for j in range(max(0, h - m), min(i, h) + 1))
        if i < h:
            dp[i] += (i - h + 1) * dp[h - 1]
    return max(dp[n], 0.0)  # clamp the result to avoid negative probabilities

print(solve())
