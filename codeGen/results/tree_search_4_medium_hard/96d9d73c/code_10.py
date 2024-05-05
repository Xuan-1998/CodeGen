import sys
from collections import defaultdict

N, K, M = map(int, input().split())
A = list(map(int, input().split()))

dp = [[False] * (K + 1) for _ in range(N + 1)]
maxprev = [0] * (K + 1)
maxprev[-1] = float('inf')

for i in range(1, N + 1):
    maxcurr = max(A[:i])
    for j in range(min(i, K), -1, -1):
        if maxcurr <= maxprev[j] + M:
            dp[i][j] = True
        else:
            break
    for j in range(K, -1, -1):
        if i >= j and (dp[i-j][j-1] or A[i-1] == maxprev[j-1]):
            dp[i][j] = True
            break

print(dp[N][K])
