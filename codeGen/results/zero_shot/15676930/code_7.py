import sys

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [0] * n
for i in range(1, n):
    dp[i] = max(dp[i-1], a[i-1]) + (a[i] if c[i-1] == 0 else b[i])
max_joy = dp[-1]
print(max_joy)
