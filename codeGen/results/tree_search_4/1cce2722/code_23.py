n = int(input())
a = list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(1, n):
    if a[i - 1] == a[i]:
        dp[i] = max(dp[i - 1], dp[i - 2]) + 3
    elif a[i - 1] == a[i] - 1 or a[i - 1] == a[i] + 1:
        dp[i] = max(dp[i - 1], dp[i - 2]) + 2
    else:
        dp[i] = max(dp[i - 1], dp[i - 2])

print(max(dp))
