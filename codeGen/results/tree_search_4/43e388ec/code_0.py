import math

# Read input and calculate max(a, b)
a = int(input(), 2)
b = int(input(), 2)
max_val = a if a > b else b

# Calculate log2(max(a, b)) for later use
log_max = math.ceil(math.log2(max_val))

dp = [0] * (314160 + 1)
for i in range(1, 314160):
    if i >= log_max:
        dp[i] = 0
    else:
        dp[i] = (dp[i-1] + ((a >> i) | (b << (i+1)))) % (10**9+7)

print(dp[314159])
