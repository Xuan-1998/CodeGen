import sys
from heapq import heappop, heappush

n = int(input())
dp = [[0] * 1000001 for _ in range(n+1)]
prev_power = -1

for _ in range(n):
    a, b = map(int, input().split())
    while True:
        if dp[a][b]:
            prev_power = b
            break
        heappush(dp[a], b)
        a -= 1

print(sum(1 for x in dp[n] if not x) - 1)
