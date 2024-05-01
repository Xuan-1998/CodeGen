import sys

# Read input numbers a and b from stdin
a = int(input(), 2)
b = int(input(), 2)

# Base case: Store initial value in dictionary for memoization
dp = {0: pow(a ^ b, (10**9 + 7), (10**9 + 7))}

# Iterate from i=1 to 314159 and update state using stored values
for i in range(1, 316228):
    dp[i] = ((dp.get(i-1, 0) if i > 0 else a ^ b) ^
             ((b >> (i % 31)) & 1))
    dp[i] %= (10**9 + 7)

# Calculate the sum of all values in the array and print result
print(sum(dp.values()) % (10**9 + 7))
