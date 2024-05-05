import sys

def infinite_zoo():
    q = int(sys.stdin.readline())
    graph = {}

    for _ in range(q):
        u, v = map(int, sys.stdin.readline().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []

        if u & v == v:
            graph[u].append(v)
        else:
            graph[u].append(~v)  # ~x is the bitwise NOT of x

    for _ in range(q):
        u, v = map(int, sys.stdin.readline().split())
        visited = set()
        stack = [u]

        while stack:
            vertex = stack.pop()
            if vertex == v:
                print("YES")
                break
            if vertex not in visited:
                visited.add(vertex)
                for neighbor in graph.get(vertex, []):
                    stack.append(neighbor)

        else:
            print("NO")

infinite_zoo()
