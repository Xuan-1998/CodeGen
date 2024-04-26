from collections import defaultdict
import sys

def dfs(graph, node, parent, label):
    global edge_labels
    for neighbor in graph[node]:
        if neighbor != parent:
            edge_labels.append((node, neighbor, label))
            dfs(graph, neighbor, node, 3 - label)  # Alternate between labels 1 and 2

def solve(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    global edge_labels
    edge_labels = []
    dfs(graph, 1, -1, 1)  # Start DFS from node 1 with label 1

    max_edges_assigned = 0
    edge_count = defaultdict(int)
    for _, _, label in edge_labels:
        edge_count[label] += 1
        max_edges_assigned = max(max_edges_assigned, edge_count[label])

    return max_edges_assigned, edge_labels

def main():
    t = int(sys.stdin.readline().strip())  # Read the number of test cases
    for _ in range(t):
        n = int(sys.stdin.readline().strip())  # Read the number of vertices
        edges = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n - 1)]
        max_edges_assigned, edge_labels = solve(n, edges)
        print(max_edges_assigned)
        for u, v, label in edge_labels:
            print(u, v, label)

if __name__ == "__main__":
    main()
