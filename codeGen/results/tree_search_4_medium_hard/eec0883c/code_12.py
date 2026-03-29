import sys
from collections import deque

def max_gasoline(n, w, roads):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i != 1:
            for road in roads[i-1:]:
                if road[0] == i:
                    j, c = road[1], road[2]
                    dp[i] = max(dp[i], dp[j] - c)
    return dp[-1]

n = int(sys.stdin.readline())
w = list(map(int, sys.stdin.readline().split()))
roads = []
for _ in range(n-1):
    u, v, c = map(int, sys.stdin.readline().split())
    roads.append([u+1, v+1, c])

print(max_gasoline(n, w, roads))
