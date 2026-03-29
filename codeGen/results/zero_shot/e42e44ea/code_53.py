import sys
from collections import deque

N, M = map(int, input().split())
grid = [[int(x) for x in input().split()] for _ in range(N)]

dp = [[0] * (M+1) for _ in range(N+1)]
for i in range(N+1):
    dp[i][0] = 0
for j in range(M+1):
    dp[0][j] = 0

q = deque([(0, 0)])
while q:
    i, j = q.popleft()
    if i < N and grid[i][j] > 0:
        dp[i][j] = min(dp[max(i-1, 0)][j], dp[i][max(j-1, 0)]) + grid[i][j]
    if i < N:
        q.append((i+1, j))
    if j < M:
        q.append((i, j+1))

print(dp[N-1][M-1])
