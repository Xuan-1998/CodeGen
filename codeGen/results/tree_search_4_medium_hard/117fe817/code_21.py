def count_ones(n):
    dp = [0] * (n + 1)
    
    for i in range(1, 10):
        dp[i] = i
    
    for i in range(10, n + 1):
        dp[i] += dp[i % 10]
    
    return sum(dp[1:])

# Read input from stdin
n = int(input())

# Calculate and print the answer
print(count_ones(n))
