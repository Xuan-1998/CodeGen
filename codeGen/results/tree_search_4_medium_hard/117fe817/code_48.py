def count_digit_ones(n):
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if i == 1:
            dp[i] = 1
        else:
            last_digit = int(str(i)[-1])
            if last_digit == 1:
                dp[i] = dp[i - 1] + 1
            elif last_digit > 1:
                dp[i] = dp[i - 1]
    
    return sum(dp)
