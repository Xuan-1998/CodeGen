from collections import defaultdict

# Function to perform DFS and find connected components
def dfs(node, graph, visited):
    visited[node] = True
    for neighbour in graph[node]:
        if not visited[neighbour]:
            dfs(neighbour, graph, visited)

# Function to count the number of connected components
def count_connected_components(graph, n):
    visited = [False] * (n + 1)
    count = 0
    for node in range(1, n + 1):
        if not visited[node]:
            dfs(node, graph, visited)
            count += 1
    return count

def main():
    # Read number of nodes and edges
    n, m = map(int, input().split())
    
    # Build the graph
    graph = defaultdict(list)
    edges = []
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
        edges.append((x, y))
    
    # Read number of experiments
    k = int(input())
    
    # Perform experiments
    for _ in range(k):
        li, ri = map(int, input().split())
        # Remove the edge for the experiment
        li_node, ri_node = edges[li - 1]
        graph[li_node].remove(ri_node)
        graph[ri_node].remove(li_node)
        
        # Count the number of connected components
        print(count_connected_components(graph, n))
        
        # Add the edge back after the experiment
        graph[li_node].append(ri_node)
        graph[ri_node].append(li_node)

if __name__ == "__main__":
    main()
