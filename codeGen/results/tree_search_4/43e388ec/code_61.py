import sys

# Read input from stdin
a = int(input(), 2)
b = int(input(), 2)

dp = [0] * (314160 % 31 + 1)  # Initialize dp array with zeros
dp[0] = a ^ b  # Base case: DP[0] = a ^ b

for i in range(1, len(dp)):
    dp[i] = (dp[(i-1)%31] ^ ((b >> (i%31)) & 1)) % (10**9 + 7)

# Calculate the sum modulo 10^9+7
result = 0
cum_sum = 0
for i in range(len(dp)):
    cum_sum += dp[i]
    result = (result + cum_sum) % (10**9 + 7)

print(result)
