n = int(input())
a = list(map(int, input().split()))
dp = [0] * n

for i in range(1, n):
    k = i - 1
    while a[k] >= a[i]:
        k -= 1
    dp[i] = max(dp[i-1], dp[k] + (k-i) + (n-k) - (a[i]-a[k]))

print(max(dp))
