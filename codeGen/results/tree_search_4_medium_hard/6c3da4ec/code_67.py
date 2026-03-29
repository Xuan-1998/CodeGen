dp = [0] * (n + 1)
for i in range(1, n + 1):
    if s[i - 1] == '1':
        dp[i] = max(dp[i-1], int(s[:i-1], 2) | int('1', 2))
    else:
        dp[i] = max(dp[i-1])
print(bin(max(dp))[2:])
