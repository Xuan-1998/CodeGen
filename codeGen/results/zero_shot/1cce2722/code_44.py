n = int(input())
a = list(map(int, input().split()))
dp = [1] * n
max_points = 0
for i in range(1, n):
    for j in range(i):
        if a[i] > a[j] and a[i] - 1 == a[j]:
            dp[i] = max(dp[i], dp[j] + 2)
    max_points = max(max_points, dp[i])
print(max_points)
