import sys

N = int(input())
A = list(map(int, input().split()))

dp = [0] * N
for i in range(1, N):
    if A[i-1] <= A[i]:
        dp[i] = dp[i-1]
    else:
        dp[i] = dp[i-1] + 1

print(dp[-1])
