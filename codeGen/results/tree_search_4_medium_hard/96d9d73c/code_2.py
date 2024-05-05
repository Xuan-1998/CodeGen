code:
import sys

N, K, M = map(int, input().split())
A = list(map(int, input().split()))

dp = [[False] * (K + 1) for _ in range(N + 1)]
prev = [0] * (K + 1)

for i in range(1, N + 1):
    for j in range(1, min(i, K) + 1):
        if dp[i - 1][j]:
            prev_val = prev[j - 1]
            dp[i][j] = any(prev_val <= A[k] and A[k] <= prev_val + M for k in range(max(0, i - j), i))
            prev[j] = max(prev[j], A[i - 1])

print(dp[N][K])
