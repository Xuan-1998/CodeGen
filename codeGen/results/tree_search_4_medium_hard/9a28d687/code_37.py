import sys
from collections import deque

n = int(sys.stdin.readline())
costs = list(map(int, sys.stdin.readline().split()))
strings = [sys.stdin.readline() for _ in range(n)]

dp = [[[[0, float('inf')]] for _ in range(2)] for _ in range(n)]
dp[0][1][0] = 0

queue = deque([(0, 1)])

while queue:
    i, j = queue.popleft()
    if dp[i][j][0] > costs[i]:
        dp[i][j][1] = min(dp[i-1][j-1][0], dp[i-1][j-1][1]) + costs[i]
    for k in range(j):
        if strings[i][k] < strings[i-1][k]:
            dp[i][j][0] = min(dp[i-1][j-1][1], dp[i-1][j-1][0]) + costs[i]
        elif strings[i][k] > strings[i-1][k]:
            dp[i][j][1] = min(dp[i-1][j-1][0], dp[i-1][j-1][1]) + costs[i]

if strings[0].lower() < strings[-1].lower():
    print(dp[n-1][0][0])
else:
    print(-1)
