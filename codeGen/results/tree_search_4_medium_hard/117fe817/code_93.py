def count_digit_one(n):
    dp = [0]*(n+1)
    
    for i in range(1, n+1):
        if i < 10:
            dp[i] = i
        else:
            last_digit = i % 10
            first_digit = (i // 10) % 10
            
            # If the last digit is 1, then all numbers with this last digit have a 1 in them.
            # So we need to add 9*last_digit + (first_digit == 1)
            dp[i] = dp[i-1]
            
            # For digits other than 1, the total number of ones they contribute is
            # equal to the number of times this digit appears in all numbers less than n.
            for j in range(10):
                if j < first_digit:
                    dp[i] += j * (9 - (j == 0) + 1)
                elif j == first_digit:
                    dp[i] += last_digit * 10 + 9
                else:
                    dp[i] += (10 - (j == 0) + 1)
    
    return sum(dp)

# Test the function
n = int(input())
print(count_digit_one(n))
