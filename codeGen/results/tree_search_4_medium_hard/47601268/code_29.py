def findNonConsecutive Ones(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        if bin(i).count('1') == len(bin(i)) - 2:  # Check if the binary representation of i has consecutive ones
            dp[i] = dp[i - 1]
        else:
            dp[i] = dp[i - 1] + 1

    return dp[n]

# Read input from stdin
n = int(input())

# Calculate and print the output
print(findNonConsecutiveOnes(n))
