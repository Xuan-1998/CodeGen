from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
dp = defaultdict(int)
max_points = 0

for k in set(a):
    i = 1
    while i <= n and a[i-1] == k:
        i += 1
    if i > 1:
        max_points = max(max_points, dp[k-1] + i - 2)
    dp[k] = max_points

print(max_points)
