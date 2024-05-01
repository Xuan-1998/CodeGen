import sys

# Read input from stdin
a = int(input())
b = int(input())

# Initialize memoization table
dp = [0] * (314160)
dp[0] = a ^ b

for i in range(1, 314160):
    dp[i] = (dp[i-1] ^ ((b >> (i-1)) & 1))

# Calculate the sum of all dp[i] values modulo 10^9+7
result = 0
for i in range(314160):
    result = (result + dp[i]) % (10**9 + 7)

print(result)
