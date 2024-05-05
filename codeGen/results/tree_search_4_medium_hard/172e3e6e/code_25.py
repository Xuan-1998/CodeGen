code = \\
from collections import defaultdict

n, *a = map(int, input().split())

dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n+1):
    for j in range(i, -1, -1):
        if a[j-1] % j == 0:
            dp[i] += dp[j-1]
            break
print((dp[n]) % (10**9 + 7))
