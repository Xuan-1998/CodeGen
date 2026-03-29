import sys
from collections import Counter

n = int(input())
M = list(map(int, input().split()))
mod = 10**9 + 7

dp = {0: 1}
res = 0
for i in range(n):
    new_dp = {}
    for j in range(i+1):
        if M[j] == i+1:
            c = Counter(M[:j])
            new_dp[i] = (new_dp.get(i, 0) + dp.get(j-1, 0) * sum((c[k] >= 1) and c[k-1] < k for k in range(1, i+2))) % mod
    res += dp.get(i, 0)
    dp = new_dp

print(res % mod)
