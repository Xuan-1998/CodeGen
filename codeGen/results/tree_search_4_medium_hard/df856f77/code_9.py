import sys

n = int(input())
A = list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(1, n):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = min(dp[i], dp[j-1] + A[j-1] - A[i])

print(dp[-1])
