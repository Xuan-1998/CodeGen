import sys

# Read input values
a = int(input())
b = int(input())

dp = [0] * (314160)

for i in range(1, 314160):
    dp[i] = (dp[i-1] + a) ^ b

result = dp[314159]
print(result % (10**9 + 7))
