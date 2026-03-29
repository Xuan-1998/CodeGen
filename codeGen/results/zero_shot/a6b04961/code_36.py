import sys

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u-1, v-1))
    return n, m, edges

def dfs(graph, vertex, visited, parent, tail, spines):
    visited.add(vertex)
    if vertex not in tail:
        tail.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            if dfs(graph, neighbor, visited, vertex, tail, spines) and neighbor not in tail:
                return True
        elif neighbor != parent:
            spines.add((parent, neighbor))
    return False

def solve(n, m, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    max_beauty = 0
    for start_vertex in range(n):
        visited = set()
        parent = None
        tail = set()
        spines = set()
        if dfs(graph, start_vertex, visited, parent, tail, spines):
            beauty = len(tail) * len(spines)
            max_beauty = max(max_beauty, beauty)

    print(max_beauty)

if __name__ == "__main__":
    n, m, edges = read_input()
    solve(n, m, edges)
