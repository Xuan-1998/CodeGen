n = int(input())
a = list(map(int, input().split()))
dp = [0] * (n + 1)
for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + a[i])
print(max(dp))
