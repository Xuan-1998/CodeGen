import sys

def read_input():
    n, m, T = map(int, [line.strip() for line in sys.stdin.readlines()][:3])
    edges = []
    for _ in range(m):
        u, v, t = map(int, sys.stdin.readline().strip().split())
        edges.append((u, v, t))
    return n, m, T, edges

def calculate_topological_sort(n, m, edges):
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n + 1)
    for u, v, t in edges:
        graph[u].append((v, t))
        indegree[v] += 1
    queue = [i for i in range(1, n+1) if indegree[i] == 0]
    topological_sort = []
    while queue:
        node = queue.pop(0)
        topological_sort.append(node)
        for neighbor, t in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return topological_sort

def calculate_maximum_number_of_vertices(n, m, T, edges):
    graph = [[] for _ in range(n+1)]
    time_limit = T
    visited = [False] * (n + 1)
    current_time = 0
    max_visited = 0
    for u, v, t in edges:
        graph[u].append((v, t))
    queue = [(1, 0)]  # (node, time)
    while queue:
        node, time = queue.pop(0)
        if visited[node]:
            continue
        visited[node] = True
        current_time += time
        if current_time > time_limit:
            break
        max_visited = max(max_visited, len([i for i in range(1, n+1) if visited[i]]))
    return max_visited

def print_output(n, m, T, edges, k):
    print(k)
    print(*[i for i in range(1, n+1) if [j for j, v, t in edges if i == j][0] < len([j for j, v, t in edges if [k for k in range(1, n+1) if visited[k]][0] == i][0])], sep=' ')

if __name__ == '__main__':
    n, m, T, edges = read_input()
    topological_sort = calculate_topological_sort(n, m, edges)
    max_visited = calculate_maximum_number_vertices(n, m, T, edges)
    print_output(n, m, T, edges, max_visited)
