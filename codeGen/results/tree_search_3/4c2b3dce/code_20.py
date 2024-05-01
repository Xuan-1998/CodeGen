import sys

s = input()
dp = {i: False for i in range(len('AB') + 1)}

for i in range(1, len('AB')):
    dp[i] = (dp[i-1] and s[:i] == 'A' * i) or any(s[j:] not in ('B' + 'A'[j:], 'A' + 'B'[j:]) for j in range(min(i, len('BA') - i)))

if all(dp.values()):
    print("YES")
else:
    print("NO")
