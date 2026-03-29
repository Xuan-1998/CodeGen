import sys

def read_input():
    n = int(sys.stdin.readline())
    graph = {}
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        if u not in graph: graph[u] = []
        if v not in graph: graph[v] = []
        graph[u].append(v)
        graph[v].append(u)  # Since it's a tree, we can assume undirected edges
    return n, graph

n, graph = read_input()

def choose_capital(graph):
    max_degree_node = max(graph, key=lambda x: len(graph[x]))
    return max_degree_node

capital = choose_capital(graph)

def calculate_reversals(graph, capital):
    reversals = 0
    for node in graph:
        if node != capital:
            # Count the number of edges that need to be reversed
            # to reach this node from the capital
            reversals = max(reversals, len(graph[node]))
    return reversals

min_reversals = calculate_reversals(graph, capital)

print(min_reversals)
capital_indexes = [i + 1 for i in range(n - 1)]
print(*capital_indexes, sep=' ')
