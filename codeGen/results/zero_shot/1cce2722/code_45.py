n = int(input())
a = list(map(int, input().split()))
dp = [0] * 105
for i in range(n):
    dp[a[i]] += 1
max_points = 0
for i in range(2, n-1):
    max_points = max(max_points, dp[a[i]] + min(dp.get(a[i]-1, 0), dp.get(a[i]+1, 0)))
print(max_points)
