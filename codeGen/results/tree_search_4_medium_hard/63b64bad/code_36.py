n = int(input())
a = list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(2, n + 1):
    x = y = 0
    for j in range(i, 1, -1):
        if x <= 0 or x > n:
            break
        x += a[j]
        y += a[j]
        x -= a[j]
        y += a[j]
    dp[i] = max(dp[i], y)

print(dp[n])
