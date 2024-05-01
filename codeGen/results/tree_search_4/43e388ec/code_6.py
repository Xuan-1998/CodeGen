import sys

# Precompute powers of 2 up to 10^9 + 7
powers = [1]
temp = 1
while temp <= 10**9 + 7:
    temp *= 2
    powers.append(temp)

def calculate_dp(a, b):
    dp = [0]
    for i in range(1, 314160):
        dp.append((dp[-1] + ((a ^ (b << i)) % (10**9+7))) % (10**9+7))
    return dp

# Read input from stdin
a = int(input())
b = int(input())

# Calculate the sum of OR operations using dynamic programming
dp = calculate_dp(a, b)
result = 0
for val in dp:
    result = (result + val) % (10**9+7)

# Print the output to stdout
print(result)
