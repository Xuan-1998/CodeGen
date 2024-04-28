m, N = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0] * (N + 1)
dp[0] = 1
for num in arr:
    for i in range(N, num - 1, -1):
        dp[i] += dp[i - num]
print(dp[-1]%1000000007)
