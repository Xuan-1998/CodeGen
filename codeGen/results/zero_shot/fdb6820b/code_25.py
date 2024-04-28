n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0] * (n + 1)
dp[0] = 1
for i in range(m):
    for j in range(n, arr[i]-1, -1):
        dp[j] += dp[j-arr[i]]
print(dp[n]%10**9+7)
