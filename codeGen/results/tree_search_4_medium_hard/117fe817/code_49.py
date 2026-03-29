def find_digits(n):
    dp = [0] * (n + 1)
    
    # Count the number of ones at each position
    for i in range(1, 10):
        if i == 1:
            dp[i * 10 - 1] += 9
        else:
            dp[i * 10 - 1] += pow(10, i-1)
            
    # Count the number of ones at each position considering tens place and others
    for i in range(10, n + 1):
        if i % 10 == 1:
            dp[i] = dp[i - 1] + (i // 10) * (pow(10, len(str(i)) - 2) - pow(10, len(str(i)) - 3))
        else:
            dp[i] = dp[i - 1]
            
    return dp[n]

n = int(input())
print(find_digits(n))
