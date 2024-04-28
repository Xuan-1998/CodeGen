import sys

# Read input from stdin
a, b = map(int, input().split())
modulo = 10**9 + 7

# Initialize memoization dictionary
dp = {0: XOR(a, 0)}

for i in range(1, 314160):
    dp[i] = dp[i-1]
    if i >= b.bit_length():
        dp[i] += XOR(a, (b << (i - b.bit_length())))
    else:
        dp[i] += dp[b.bit_length() - 1]

# Calculate the final result
result = dp[314159]

print(result % modulo)
