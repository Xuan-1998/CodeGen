def max_grade(n, t):
    dp = [[0] * (t + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, t + 1):
            if j >= 9:  # If there are more than 9 seconds left, we can round the whole decimal fraction
                dp[i][j] = (i // 2) * (10 ** i)  # The maximum grade is the integer part of the decimal fraction multiplied by 10 raised to the power of the number of digits after the decimal point
            else:
                max_grade_without_rounding = int((dp[i - 1][j - 1] + 1e-9)) * (10 ** i)  # The maximum grade without rounding is the integer part of the previous grade multiplied by 10 raised to the power of the number of digits after the decimal point
                max_grade_with_rounding = dp[i][j - 1] + (i // 2) * (10 ** (i - 1))  # The maximum grade with rounding is the previous grade plus the integer part of the decimal fraction multiplied by 10 raised to the power of one less than the number of digits after the decimal point
                dp[i][j] = max(max_grade_without_rounding, max_grade_with_rounding)  # The maximum grade is the maximum of the maximum grade without rounding and the maximum grade with rounding
    
    return int(dp[-1][-1])  # Return the maximum grade

if __name__ == "__main__":
    n, t = map(int, input().split())
    print(max_grade(n, t))
