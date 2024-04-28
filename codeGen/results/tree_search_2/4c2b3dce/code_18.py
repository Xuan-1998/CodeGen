import sys

s = input()
dp = [True]
for i in range(1, len(s)):
    dp.append(False)

for i in range(2, len(s)):
    if s[i-2:i] == 'BA' and (i >= 5 and s[i-5:i-2] == 'AB'):
        for j in range(i):
            dp[j] = True

print('YES' if any(dp) else 'NO')
