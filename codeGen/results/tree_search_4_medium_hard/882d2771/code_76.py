import sys

# Define the modulo value
MOD = 10**9 + 7

def f(l, r):
    # Initialize the dp array with f(1) values
    dp = [0] * (r - l + 2)
    dp[0] = 0

    for i in range(1, r - l + 2):
        if i == 1:
            dp[i] = t0
        else:
            dp[i] = (t0 * f(l) + t1 * f(l+1) % MOD - l * f(r)) % MOD

    return dp[r-l+1]

# Read inputs from stdin
t, l, r = map(int, input().split())

# Initialize the coefficients
t0, t1 = 0, 0

# Calculate and print the result
print(f(l, r))
