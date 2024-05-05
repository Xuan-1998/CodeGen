def has_consecutive_ones(n):
    # Check if the binary representation of n has consecutive ones
    return str(bin(n))[2:].replace('0', '').count('1') > 1

dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
    if not has_consecutive_ones(i):
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = min(dp[i - 1], 1 + sum(dp[j - 1] for j in range(1, i) if not has_consecutive_ones(j)))

print(dp[n])
