import sys

# Read input and calculate a, b
a = int(input(), 2)
b = int(input(), 2)

DP = [0] * (314160)  # Initialize DP array with zeros
DP[0] = a ^ b  # Base case: DP[0] is the sum modulo (10**9 + 7) of a and b

for i in range(1, 314160):
    DP[i] = ((a >> i) & 1) ^ ((b >> i) & 1)  # Calculate DP[i]
    DP[i] %= (10**9 + 7)

# Calculate the sum modulo (10**9 + 7)
sum_result = 0
for i in range(314159):
    sum_result += DP[i]
sum_result %= (10**9 + 7)

print(sum_result)
