import sys

# Read inputs from stdin
a, b = map(int, input().split())

k = 19
j = 314159

dp = [[0] * (j + 1) for _ in range(k + 1)]

for i in range(2**k):
    a_bin = bin(i)[2:].zfill(k)
    for j in range(j + 1):
        b_bin = bin(b)[2:].zfill(j + 1)
        dp[k][j] += int(a_bin, 2) | (int(b_bin, 2) << i)

# Calculate the final answer
result = sum(dp[-1]) % (10**9 + 7)

print(result)
