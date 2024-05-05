code
n = int(input())
s = input()
dp = [0] * (n + 1)
max_val = 0

for i in range(1, n + 1):
    if s[i - 1] == '1':
        dp[i] = max(dp[i-1], max_val) | 1
    else:
        dp[i] = dp[i-1]
    max_val = dp[i]

print(bin(max_val)[2:].zfill(n))
