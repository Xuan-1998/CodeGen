import sys

def dfs(graph, node, parent, visited, stack):
    visited[node] = True
    stack.append(node)
    for neighbor, length in graph[node]:
        if not visited[neighbor]:
            if dfs(graph, neighbor, node, visited, stack):
                return True
        elif neighbor != parent:
            # Found a cycle
            return True
    stack.pop()
    return False

def find_cycle(graph, n):
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            stack = []
            if dfs(graph, i, -1, visited, stack):
                return stack
    return None

def solve(n, roads):
    graph = [[] for _ in range(n)]
    total_length = 0
    for u, v, l in roads:
        graph[u-1].append((v-1, l))
        graph[v-1].append((u-1, l))
        total_length += l

    cycle = find_cycle(graph, n)
    if not cycle:
        return total_length

    max_road_length = 0
    for i in range(len(cycle) - 1):
        u, v = cycle[i], cycle[i+1]
        for neighbor, length in graph[u]:
            if neighbor == v:
                max_road_length = max(max_road_length, length)
                break

    # The last edge of the cycle
    u, v = cycle[-1], cycle[0]
    for neighbor, length in graph[u]:
        if neighbor == v:
            max_road_length = max(max_road_length, length)
            break

    return total_length - max_road_length

# Read input
n = int(input().strip())
roads = [tuple(map(int, input().strip().split())) for _ in range(n)]

# Solve the problem and output the result
print(solve(n, roads))
