import sys
from collections import deque

n = int(input())
a = list(map(int, input().split()))
dp = [0] * (n + 1)

for k in range(1, n):
    if a[k] == a[k-1]:
        dp[k+1] = max(dp[k+1], dp[k] + 1)
    else:
        for j in range(k-1, -1, -1):
            if abs(a[j] - a[k]) in (1, k-1, k):
                dp[k+1] = max(dp[k+1], dp[j] + 1)
                break

print(max(dp))
