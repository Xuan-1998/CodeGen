import sys

# Read input integers
a = int(input(), 2)
b = int(input(), 2)

max_bits = len(bin(a)) - 2  # subtracting 1 for leading '0' and 1 for trailing '\n'
dp = dict((i, {j: 0 for j in range(max_bits + 1)}) for i in range(max_bits + 1))

for i in range(1, max_bits + 1):
    for j in range(i, -1, -1):
        if j > i:
            dp[i][j] = (dp[i-1].get(j % (i+1), 0) if j % (i+1) else 0)
        else:
            dp[i][j] = ((a >> i) ^ b) * pow(2, i)

# Compute and print the sum modulo (10^9 + 7)
result = sum(dp[i].values() for i in range(max_bits + 1))
print(result % (10**9 + 7))
