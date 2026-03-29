import sys

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(1, n):
    dp[i] = max(dp[i-1], dp[i-2] + a[i]) if i % 2 == 1 else max(dp[i-1], dp[i-2] + c[i])

print(max(dp))
