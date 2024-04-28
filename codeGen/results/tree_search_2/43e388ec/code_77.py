import sys

# Define the modulo value
MOD = 10**9 + 7

def left_shift(x, i):
    return x << i

d = {}  # Dictionary to store previously computed values

def xor_left_shift(a, b, k):
    dp = [0] * (k + 1)
    for i in range(k + 1):
        if i == 0:
            dp[i] = a ^ b
        else:
            dp[i] = (dp[i-1] + d.get((a << i) ^ b, 0)) % MOD
    return sum(dp)

# Read input from stdin
a = int(input())
b = int(input())

k = 314159

print(xor_left_shift(a, b, k))
