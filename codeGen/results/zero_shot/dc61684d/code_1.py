from collections import defaultdict

def dfs(graph, visited, node):
    visited[node] = True
    for neighbour in graph[node]:
        if not visited[neighbour]:
            dfs(graph, visited, neighbour)

def count_components(graph, n):
    visited = [False] * (n + 1)
    components = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(graph, visited, i)
            components += 1
    return components

def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    edges = []

    # Building the graph and storing edges
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
        edges.append((x, y))

    k = int(input())

    # Processing experiments
    for _ in range(k):
        li, ri = map(int, input().split())
        # Remove the edge for the experiment
        graph[edges[li - 1][0]].remove(edges[li - 1][1])
        graph[edges[ri - 1][1]].remove(edges[ri - 1][0])
        
        # Count the components
        print(count_components(graph, n))
        
        # Add the edge back to the graph
        graph[edges[li - 1][0]].append(edges[li - 1][1])
        graph[edges[ri - 1][1]].append(edges[ri - 1][0])

if __name__ == "__main__":
    main()
