n = int(input())
a = list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(2, n):
    dp[i] = min(dp[i-1], dp[i-2]) if a[i] != a[i-1] and a[i] != a[i-2] else dp[i-1] + 1

print(n - max(dp))
