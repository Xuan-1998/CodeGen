import sys
from collections import defaultdict

n = int(sys.stdin.readline())
graph = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)

dp = [float('inf')] * (n+1)
parent = [-1] * (n+1)
dp[0] = 0

for i in range(1, n+1):
    for j in graph[i]:
        if dp[j] + 1 < dp[i]:
            dp[i] = dp[j] + 1
            parent[i] = j

ans = 0
capital = []
visited = set()
def dfs(i):
    global ans, capital
    visited.add(i)
    while i != 0:
        capital.append(i)
        i = parent[i]
    ans = len(capital)

dfs(n-1)

sys.stdout.write(str(ans) + '\n')
for city in capital[::-1]:
    sys.stdout.write(str(city) + ' ')
sys.stdout.write('\n')

