import sys

n = int(input())
A = list(map(int, input().split()))

dp = [[float('inf')] * (max(A) + 1) for _ in range(n)]
for i in range(1, n):
    for j in range(max(A) + 1):
        if not any(k <= j for k in A[:i]):
            dp[i][j] = dp[i-1].index(min(k for k in A[:i] if k <= j))
        else:
            prev_index = dp[i-1].index(min(k for k in A[:i] if k <= j))
            prev_diff = j - A[prev_index]
            dp[i][j] = dp[i-1][prev_index] + (0 if j == A[prev_index] else 1)

min_ops = min(dp[-1])
print(min_ops)
