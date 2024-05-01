n = int(input())
a = list(map(int, input().split()))
dp = [0] * (n+1)
for i in range(1, n+1):
    max_points = 0
    for j in range(i):
        if a[j] == i:
            max_points = dp[j] + n - j
            break
    dp[i] = max(dp[i-1], max_points)
print(dp[-1])
