def count_digit_ones(n):
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if i < 10:  # Single-digit numbers
            dp[i] = 1
        elif i % 10 == 0:  # Numbers ending with 0
            dp[i] = dp[i // 10]
        else:
            last_digit = (i % 10)
            if last_digit == 1:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i - 1]
    
    return sum(dp)

n = int(input())
print(count_digit_ones(n))
