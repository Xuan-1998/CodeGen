import sys
from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

dp = [0] * (n + 1)
memo = defaultdict(int)

for i in range(n):
    for k in range(i):
        if k > 0 and k < i:
            memo[i] = max(memo.get(i, 0), dp[k] - abs(a[i] - a[k]) + n - i)
    dp[i] += memo.get(i, 0)

print(max(dp))
