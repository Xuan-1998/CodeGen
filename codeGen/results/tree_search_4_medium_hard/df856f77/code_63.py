code
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [0] * (N + 1)
for i in range(1, N + 1):
    min_ops = float('inf')
    for j in range(1, i + 1):
        if A[j - 1] > A[i]:
            max_val = max(A[:j])
            min_ops = min(min_ops, i - j)
    dp[i] = dp[i - 1] + min_ops

print(dp[N])
code
