import sys
from collections import defaultdict

def dfs(node, parent, graph, visited, stack):
    visited[node] = True
    stack[node] = True
    for neighbor, weight in graph[node]:
        if not visited[neighbor]:
            if dfs(neighbor, node, graph, visited, stack):
                return True, weight
        elif stack[neighbor] and neighbor != parent:
            # Found a cycle, return the weight of the edge causing the cycle
            return True, weight
    stack[node] = False
    return False, None

def find_min_inconvenience(n, roads):
    graph = defaultdict(list)
    for u, v, l in roads:
        graph[u].append((v, l))
        graph[v].append((u, l))

    visited = [False] * (n + 1)
    stack = [False] * (n + 1)
    min_inconvenience = float('inf')

    for i in range(1, n + 1):
        if not visited[i]:
            found_cycle, cycle_weight = dfs(i, -1, graph, visited, stack)
            if found_cycle:
                min_inconvenience = min(min_inconvenience, cycle_weight)

    return min_inconvenience

def main():
    n = int(sys.stdin.readline().strip())
    roads = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    result = find_min_inconvenience(n, roads)
    print(result)

if __name__ == "__main__":
    main()
