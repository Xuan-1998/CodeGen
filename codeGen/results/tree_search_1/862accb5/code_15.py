import sys

def dfs(graph, node, parent, visited, stack):
    visited[node] = True
    stack.append(node)
    
    for child, length in graph[node]:
        if not visited[child]:
            if dfs(graph, child, node, visited, stack):
                return True
        elif child != parent:
            # Cycle detected
            return True
    
    stack.pop()
    return False

def find_cycle(graph, n):
    visited = [False] * (n + 1)
    stack = []
    
    for i in range(1, n + 1):
        if not visited[i]:
            if dfs(graph, i, -1, visited, stack):
                return stack
    return []

def calculate_inconvenience(graph, cycle):
    cycle_length = sum(graph[u][v] for u, v in zip(cycle, cycle[1:] + [cycle[0]]))
    min_inconvenience = float('inf')
    
    for i in range(len(cycle)):
        u, v = cycle[i], cycle[(i + 1) % len(cycle)]
        road_length = graph[u][v]
        inconvenience = cycle_length - road_length
        min_inconvenience = min(min_inconvenience, inconvenience)
    
    return min_inconvenience

def main():
    n = int(sys.stdin.readline().strip())
    graph = {i: [] for i in range(1, n + 1)}

    for _ in range(n):
        u, v, l = map(int, sys.stdin.readline().split())
        graph[u].append((v, l))
        graph[v].append((u, l))

    cycle = find_cycle(graph, n)
    result = calculate_inconvenience(graph, cycle)
    
    print(result)

if __name__ == "__main__":
    main()
