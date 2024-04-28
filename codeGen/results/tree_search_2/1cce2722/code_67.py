n = int(input())
a = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    if i == 0:
        dp[i] = 1 if a[0] == 1 else 0
    elif i == 1:
        dp[i] = 1 if (a[i-1] + 1) % 3 == 0 or (a[i-1] - 1) % 3 == 0 else 0
    else:
        if a[i] == a[i-1] + 1 or a[i] == a[i-1] - 1:
            dp[i] = max(dp[i-1], dp[i-2])
        else:
            dp[i] = dp[i-1]
