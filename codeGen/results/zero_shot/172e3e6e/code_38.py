import sys

def good_subsequences(n, a):
    # Initialize dp array with zeros
    dp = [0] * (n + 1)

    # Base case: The number of good subsequences for an empty subsequence is 1
    dp[0] = 1

    # Iterate over the array
    for i in range(n):
        # If a_i is divisible by i+1, update dp[i+1]
        if (a[i] % (i + 1) == 0):
            dp[i + 1] += dp[i]

    # Return the number of good subsequences modulo 10^9 + 7
    return sum(dp) % (10**9 + 7)

# Read input from stdin
n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))

# Calculate and print the result
result = good_subsequences(n, a)
print(result)
