def count_digits(n):
    dp = [0] * 10
    for i in range(1, n+1):
        last_digit = (i % 10)
        if last_digit == 1:
            dp[0] += 1
        else:
            dp[last_digit] += 1
    return sum(dp)
