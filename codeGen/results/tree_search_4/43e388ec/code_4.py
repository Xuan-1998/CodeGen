dp = {0: 0} # base case
for i in range(1, 314160):
    dp[i] = ((dp.get((i-1)%314159, 0) + (a & (1 << i%10)) - (b >> (i%10))) % 1000000007)
print(sum(dp.values()) % 1000000007)
