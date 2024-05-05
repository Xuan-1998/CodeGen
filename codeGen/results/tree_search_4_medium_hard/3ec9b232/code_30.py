import sys
from collections import defaultdict

n = int(input())
M = list(map(int, input().split()))
dp = [[0]*n for _ in range(n)]

for i in reversed(range(n)):
    for j in range(i+1):
        if M[j] == i+1:
            dp[i][j] = 1
        elif j > 0 and M[j-1] == i+1:
            dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = sum(dp[k][j-1] if k < i else 1 for k in range(i+1))

res = sum(dp[i][n-1] for i in range(n))
print(res % (10**9 + 7))
