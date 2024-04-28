k, n = map(int, input().split())
dp = [0] * (n+1)
dp[1] = 1

for i in range(2, n+1):
    dp[i] = sum(dp[j] for j in range(1, i//i+1) if i % j == 0)

result = sum(dp[i] for i in range(k+1))
print(result % 10000007)
