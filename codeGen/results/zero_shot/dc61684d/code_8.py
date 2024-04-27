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
            components += 1
            dfs(graph, visited, i)
    return components

def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    edges = []

    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
        edges.append((x, y))

    k = int(input())
    experiments = [tuple(map(int, input().split())) for _ in range(k)]

    for li, ri in experiments:
        # Remove the edge
        graph[edges[li - 1][0]].remove(edges[li - 1][1])
        graph[edges[li - 1][1]].remove(edges[li - 1][0])
        
        # Count and print the number of connected components
        print(count_components(graph, n))
        
        # Add the edge back
        graph[edges[li - 1][0]].append(edges[li - 1][1])
        graph[edges[li - 1][1]].append(edges[li - 1][0])

if __name__ == "__main__":
    main()
