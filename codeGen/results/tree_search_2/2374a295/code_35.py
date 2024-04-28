def is_divisible(i):
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            return True
    return False

n, k = map(int, input().split())
dp = [[0] * (k+1) for _ in range(n+1)]
for i in range(1, n+1):
    dp[i][0] = 1
for i in range(1, n+1):
    for j in range(1, min(i, k)+1):
        if is_divisible(i):
            dp[i][j] += dp[i-1][j-1]
        dp[i][j] %= 1000000007

print(dp[n][k])
