def good_subsequences(n, a):
    dp = {(0, set()): 1}
    for i in range(1, n):
        prev_dp_values = list(dp.values())
        del prev_dp_values[0]
        for prev_divisors, val in zip(prev_dp_values, dp.keys()):
            prev_max_divisor = max(prev_divisors)
            if a[i] % prev_max_divisor == 0:
                new_divisors = set(prev_divisors) | {i}
                dp[new_divisors] = (dp.get(new_divisors, 0) or val) + val
    return sum(val for key, val in dp.items()) % (10**9 + 7)
