import sys

# Input values for a and b
a = int(input(), 2)
b = int(input(), 2)

mod = 10**9 + 7

dp = [0] * (314160)  # Initialize dp array with zeros
dp[0] = a

for i in range(1, 314160):
    if (a >> i) & 1:  # Check the ith bit of a
        dp[i] = ((dp[i-1] - (1 << i)) + b) % mod
    else:
        dp[i] = dp[i-1]

print(dp[314159] % mod)
