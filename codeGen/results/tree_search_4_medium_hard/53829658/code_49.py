import sys
from collections import defaultdict

def dijkstra(graph, start):
    visited = set()
    distance = {node: float('inf') for node in graph}
    distance[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distance[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                old_distance = distance[neighbor]
                new_distance = current_distance + weight
                if new_distance < old_distance:
                    distance[neighbor] = new_distance
                    heapq.heappush(pq, (new_distance, neighbor))
        visited.add(current_node)

    return distance

def find_capital(graph):
    n = len(graph)
    dp = [0] * (n + 1)
    memo = {}

    def dfs(node):
        if node in memo:
            return memo[node]
        min_dist = float('inf')
        for neighbor, weight in graph[node].items():
            dist = weight + dfs(neighbor)
            min_dist = min(min_dist, dist)
        dp[node] = min_dist
        memo[node] = min_dist
        return min_dist

    max_dist = 0
    capital = -1
    for node in range(1, n + 1):
        if dfs(node) > max_dist:
            max_dist = dfs(node)
            capital = node

    return dp[capital], ' '.join(map(str, list(range(1, n + 1))))

n = int(input())
graph = defaultdict(dict)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 0

print(*find_capital(graph), sep='\n')
