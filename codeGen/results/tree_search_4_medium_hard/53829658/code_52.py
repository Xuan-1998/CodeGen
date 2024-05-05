import sys
from collections import defaultdict

n = int(input())
graph = defaultdict(list)
dp = [[float('inf')] * n for _ in range(n)]
parent = [0] * n

for i in range(1, n):
    a, b = map(int, input().split())
    graph[a].append(b)
    dp[i][i-1] = 1

def dfs(node):
    for neighbor in graph[node]:
        if dp[neighbor][node - 1] == float('inf'):
            parent[neighbor] = node
            dfs(neighbor)

dfs(0)

for i in range(n):
    print(dp[-1][i], end=' ')

print()

capitals = [0]
cur_capital = 0

while cur_capital < n:
    for i in range(cur_capital + 1, n):
        if parent[i] == cur_capital:
            capitals.append(i)
            break
    cur_capital = i

for capital in capitals:
    print(capital, end=' ')
