===BEGIN CODE===
import sys
n = int(input())
s = input()

dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = dp[i - 1]
    for j in range(i):
        if s[j] == '1' and s[i-1] == '1':
            dp[i] = max(dp[i], dp[j] | (1 << (i - j - 1)))
print(bin(max(0, dp[-1])).replace("0b", ""))
