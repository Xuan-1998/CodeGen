import sys
from heapq import heapify, heappop

m = int(input())
A = [list(map(int, input().split())) for _ in range(m)]
dp = [[0] * m for _ in range(m)]

for i in range(m):
    dp[i][0] = A[i][0]
heapify([(dp[0][j], j) for j in range(1, m)])

for i in range(1, m):
    for j in range(m):
        if j == 0:
            dp[i][j] = A[i][j]
        else:
            dp[i][j] = A[i][j] + heappop(heap)[0]

print(min(dp[m-1]))
