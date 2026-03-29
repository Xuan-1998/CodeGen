===BEGIN CODE===
from collections import defaultdict

n = int(input())
s = input()

dp = defaultdict(int)
for i in range(n):
    for j in range(i+1):
        if s[j] == '0':
            left_or = 0
        else:
            left_or = (1 << (i-j))
        
        right_or = 0
        for k in range(j, i):
            right_or |= 1 if s[k] == '1' else 0
        
        dp[i+1] = max(dp.get(i, 0), left_or | right_or)

print(bin(max(dp.values()))[2:].zfill(n).lstrip('0'))
===END CODE===
