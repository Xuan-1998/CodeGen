n = int(input())
s = input()

dp = [0] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    max_val = 0
    for j in range(i):
        or_val = dp[j] | (int(s[i - 1]) << (i - j - 1))
        if or_val > max_val:
            max_val = or_val
    dp[i] = max_val

max_or = 0
for i in range(n, -1, -1):
    if dp[i] != 0 and ((dp[i] << (n - i)) & 1) == 0:
        max_or = dp[i]
        break

print(bin(max_or)[2:])
