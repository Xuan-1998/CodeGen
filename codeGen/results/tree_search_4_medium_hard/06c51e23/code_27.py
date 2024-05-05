import sys
from collections import deque

dp = [[0] * 1000001 for _ in range(200001)]
f = float(sys.stdin.readline())
n = int(sys.stdin.readline())

q = deque([(n, f)])
while q:
    i, f = q.popleft()
    if i == 0:
        print(int(f * 10))
        break
    dp[i][int(f * 10)] = max(dp[i-1][int(f * 10)], round(f) - dp[i-1][round(f)])
    for j in range(10):
        q.append((i-1, f + (j/10.0)))
