a, b = [int(x) for x in input().split()]
prefix_or = 0
suffix_or = 0
dp = [0] * (314160)
for i in range(314160):
    if i == 0:
        prefix_or = a & 1
    else:
        prefix_or = (prefix_or << 1 | ((a >> i) & 1)) % (10**9 + 7)
    dp[i] = (dp[i-1] + prefix_or) % (10**9 + 7)
    if i > 0:
        suffix_or = (suffix_or << 1 | b[i-1]) % (10**9 + 7)
        dp[i] = (dp[i-1] + suffix_or) % (10**9 + 7)
print(dp[314159])
