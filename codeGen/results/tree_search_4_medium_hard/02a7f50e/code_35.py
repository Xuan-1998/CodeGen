code
n = int(input())
dp = [0] * (n + 1)
for i in range(n):
    dp[i+1] = max(dp[i], b_i - dp[i-1])
print(min(dp))
