m, n = map(int, input().split())
dp = [0] * (n + 1)
for i in range(m):
    for j in range(n, -1, -1):
        dp[j] += 1
print((pow(10,9) + 7)**-1 * sum(dp))
