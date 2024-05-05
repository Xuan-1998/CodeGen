from collections import deque

def max_gasoline(n, w, roads):
    graph = [[] for _ in range(n)]
    for u, v, c in roads:
        graph[u].append((v, -c))
        graph[v].append((u, c))

    max_gas = [0] * n
    visited = set()

    def dfs(node, remaining_gas):
        if node not in visited:
            visited.add(node)
            for neighbor, edge_gas in graph[node]:
                if edge_gas < 0 and remaining_gas - abs(edge_gas) >= 0:
                    remaining_gas -= abs(edge_gas)
                    max_gas[neighbor] = max(max_gas[neighbor], dfs(neighbor, remaining_gas))
                elif edge_gas > 0 and remaining_gas + edge_gas <= w[neighbor]:
                    remaining_gas += edge_gas
                    max_gas[neighbor] = max(max_gas[neighbor], dfs(neighbor, remaining_gas))
            return max_gas[node]
        return 0

    return max(max_gas)

n = int(input())
w = list(map(int, input().split()))
roads = [list(map(int, input().split())) for _ in range(n-1)]

print(max_gasoline(n, w, roads))
