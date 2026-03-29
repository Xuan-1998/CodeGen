dp = [0] * (n + 1)

for i in range(1, n + 1):
    rounding_gain = round(0.01 * (10 ** (n - i)))
    not_rounding_gain = dp[i - 1]
    
    if rounding_gain > 0:
        dp[i] = max(dp[i - 1], 9.99 * (10 ** (n - i)) + rounding_gain)
    else:
        dp[i] = dp[i - 1]

max_grade = dp[-1]
print(int(max_grade))
