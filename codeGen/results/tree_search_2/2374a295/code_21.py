def is_divisible(n, k):
    return k % n == 0


dp = [0]*(n+1)
for i in range(1, n+1):
    dp[i] = 1

for i in range(1, n+1):
    for j in range(i, min(i+k, n+1)):
        if is_divisible(j, i):
            dp[i][j] += dp[i-1][j-i]

print(sum(dp[n])[k%1000000007])
