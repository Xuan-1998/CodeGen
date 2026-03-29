import sys
from collections import defaultdict

def dfs(node, gas_left, memo):
    if node not in memo:
        max_gas = min(gas_left, memo[node]['max_gas'])
        for neighbor, weight in graph[node].items():
            max_gas = max(max_gas, dfs(neighbor, min(gas_left + weight, memo[neighbor]['max_gas']), memo))
        memo[node] = {'max_gas': max_gas}
    return memo[node]['max_gas']

def solve(graph):
    n = len(graph)
    start, end = 0, n - 1
    memo = defaultdict(dict)

    for node in graph:
        gas_left = w[node]
        memo[node]['max_gas'] = gas_left

    max_gas = dfs(start, 0, memo)
    return max_gas

# Input: Read from standard input
n = int(input())
w = list(map(int, input().split()))
graph = defaultdict(dict)

for _ in range(n - 1):
    u, v, c = map(int, input().split())
    graph[u][v] = c
    graph[v][u] = c

print(solve(graph))
