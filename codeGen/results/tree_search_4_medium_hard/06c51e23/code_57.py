def max_grade(n, t, fractional_part):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        fractional_part_i = int(fractional_part[:i+1])
        round_value = round(fractional_part_i)
        dp[i] = max(dp[i-1], round_value)
    return dp[n]
