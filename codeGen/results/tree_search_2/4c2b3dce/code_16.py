import sys

n = int(input())
s = input()

dp = [False] * (n + 1)
dp[0] = True

for i in range(1, n):
    dp[i] = False
    if i >= 2 and s[i-2:i] == 'BA' and (i >= 4 and s[i-4:i-2] == 'AB'):
        dp[i] = True

print('YES' if dp[-1] else 'NO')
