from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
dp = [0] + [float('inf')] * (n - 1)
last = float('-inf')
for i in range(n):
    while a[i] <= last:
        dp[i] = min(dp[i], dp[i-1] + 1)
        last -= 1
    last = a[i]
print(min(dp))
