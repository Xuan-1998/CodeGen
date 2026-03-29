code_block
n = int(input())
p = [int(x) for x in input().split()]
dp = [0] * (n + 1)
for i in range(1, n + 1):
    if i % 2 == 1:
        dp[i] = min(dp[p[i - 1]], 1 + dp[i - 1])
    else:
        dp[i] = 1 + dp[(i + 1) // 2]
print((dp[n] % (10**9 + 7)))
