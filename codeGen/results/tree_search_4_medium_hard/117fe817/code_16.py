def find_digits_one(n):
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if i < 10:
            dp[i] = 1
        else:
            for j in range(10**(i-1), 2*10**(i-1)):
                dp[i] += 1
                
    return sum(dp)

# Read the input from stdin
n = int(input())

# Calculate and print the result
print(find_digits_one(n))
