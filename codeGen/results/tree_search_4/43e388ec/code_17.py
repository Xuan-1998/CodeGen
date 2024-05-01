import sys

# Read input from stdin
a = int(input())
b = int(input())

# Initialize dp array with size 315160
dp = [0] * (315160 + 1)
dp[0] = a ^ b

for i in range(1, 314159):
    dp[i] = (a ^ (b << i)) | dp[i-1]

print((dp[314159]) % (10**9 + 7))
