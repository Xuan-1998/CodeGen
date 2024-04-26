import sys

def dfs(node, parent, graph, visited, edges_in_cycle):
    visited[node] = True
    for neighbor, weight in graph[node]:
        if not visited[neighbor]:
            edges_in_cycle.append((weight, node, neighbor))
            if dfs(neighbor, node, graph, visited, edges_in_cycle):
                return True
        elif neighbor != parent:
            # Found a cycle
            edges_in_cycle.append((weight, node, neighbor))
            return True
    edges_in_cycle.pop()
    return False

def find_max_edge_in_cycle(edges_in_cycle):
    return max(edges_in_cycle)

def main():
    n = int(sys.stdin.readline().strip())
    graph = {i: [] for i in range(1, n+1)}
    total_inconvenience = 0
    
    for _ in range(n):
        u, v, l = map(int, sys.stdin.readline().strip().split())
        graph[u].append((v, l))
        graph[v].append((u, l))
        total_inconvenience += l
    
    visited = [False] * (n + 1)
    edges_in_cycle = []
    
    # Assuming the graph is connected and there's at least one cycle
    dfs(1, -1, graph, visited, edges_in_cycle)
    
    # Find the maximum edge in the cycle
    max_edge_weight, _, _ = find_max_edge_in_cycle(edges_in_cycle)
    
    # Calculate the result
    result = total_inconvenience - max_edge_weight
    print(result)

if __name__ == "__main__":
    main()
