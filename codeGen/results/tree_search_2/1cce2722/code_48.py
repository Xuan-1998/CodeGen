import sys

n = int(input())
a = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    if (i > 0 and a[i] == a[i-1]) or (i < n-1 and a[i] == a[i+1]):
        dp[i] = 1 + min(dp[max(0, i-2)], dp[min(n, i+2)])
    else:
        dp[i] = n

print(max(dp))
