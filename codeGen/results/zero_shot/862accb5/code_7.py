import sys
from collections import defaultdict

def dfs(graph, node, parent, depth, visited, back_edges):
    visited[node] = depth
    for neighbor, length in graph[node]:
        if neighbor == parent:
            continue
        if visited[neighbor] == -1:
            back_edges[neighbor] = (node, length)
            if dfs(graph, neighbor, node, depth + 1, visited, back_edges):
                return True
        elif visited[neighbor] < visited[node] - 1:
            # Found a cycle
            back_edges[node] = (neighbor, length)
            return True
    return False

def find_cycle(graph, n):
    visited = [-1] * n
    back_edges = {}
    for i in range(n):
        if visited[i] == -1:
            if dfs(graph, i, -1, 0, visited, back_edges):
                break
    # Reconstruct the cycle
    cycle = []
    node, length = back_edges[i]
    cycle.append(length)
    while node != i:
        next_node, length = back_edges[node]
        cycle.append(length)
        node = next_node
    return cycle

def main():
    n = int(sys.stdin.readline())
    graph = defaultdict(list)
    total_length = 0
    for _ in range(n):
        u, v, l = map(int, sys.stdin.readline().split())
        graph[u-1].append((v-1, l))
        graph[v-1].append((u-1, l))
        total_length += l
    
    cycle = find_cycle(graph, n)
    longest_road = max(cycle)
    min_inconvenience = total_length - longest_road

    print(min_inconvenience)

if __name__ == "__main__":
    main()
