import sys

def solve(n):
    # Create an adjacency list representation of the DAG
    graph = [[] for _ in range(n + 1)]

    for i in range(2, n + 1):
        for j in range(i - 1, 0, -1):
            graph[j].append(i)
            if len(graph[i]) > 0:
                break

    # Perform topological sorting using DFS
    visited = [False] * (n + 1)
    order = []

    def dfs(node):
        if not visited[node]:
            visited[node] = True
            for neighbor in graph[node]:
                dfs(neighbor)
            order.append(str(node))

    for node in range(1, n + 1):
        if not visited[node]:
            dfs(node)

    # Print the result
    print(' '.join(order))

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    solve(n)
