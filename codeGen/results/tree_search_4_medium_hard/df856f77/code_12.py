code
import sys

N = int(input())
A = list(map(int, input().split()))

dp = [0] * (N + 1)
for i in range(1, N):
    if A[i] >= A[i-1]:
        dp[i] = dp[i-1]
    else:
        dp[i] = dp[i-1] + 1

print(dp[N])
