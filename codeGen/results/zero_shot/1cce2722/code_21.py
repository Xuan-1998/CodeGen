n = int(input())
a = list(map(int, input().split()))
dp = [0] * (n + 1)
dp[0] = float('-inf')
for i in range(n):
    dp[i+1] = max(dp[i], a[i] - dp[i])
print(max(dp))
