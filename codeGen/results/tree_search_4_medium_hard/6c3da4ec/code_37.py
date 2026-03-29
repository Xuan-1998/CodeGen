import sys

n = int(input())
s = input()

dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = 0
    for j in range(i):
        for k in range(j + 1, i):
            if s[j] == '1' and s[k] == '1':
                dp[i] = max(dp[i], dp[j] | (1 << (i - j - 1)) | int(s[k]) << k)

print(bin(max((dp[i] for i in range(1, n + 1)), default=0)).lstrip('0').or_(''))
