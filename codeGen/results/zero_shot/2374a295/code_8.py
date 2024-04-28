n, k = map(int, input().split())
dp = [0] * (k + 1)
dp[0] = 1
for i in range(1, k):
    dp[i] = ((i % n) * (dp[i-1] % 1000000007)) % 1000000007
print((dp[k-1]))
