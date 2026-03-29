import sys

def xor_of_node_values(node, parent, node_values):
    if node == 0:
        return 0
    if node_values[node] == -1:
        return xor_of_node_values(parent, node, node_values)
    for neighbor in graph[node]:
        if neighbor != parent:
            node_values[neighbor] = -1
    return node_values[node]

def is_possible_to_delete_edges(k):
    node_values = [0] * (n + 1)
    for i in range(1, n + 1):
        node_values[i] = a[i]
    
    # Perform DFS to calculate the bitwise XOR of each subtree
    for i in range(1, n):
        parent, child = graph[i]
        node_values[child] = xor_of_node_values(child, parent, node_values)
        
    # Check if it's possible to delete at most k-1 edges
    for i in range(1, n + 1):
        if node_values[i] != 0:
            return "NO"
            
    return "YES"

# Read input and process each test case
t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    graph = {}
    for i in range(n - 1):
        ui, vi = map(int, sys.stdin.readline().split())
        if ui not in graph:
            graph[ui] = []
        if vi not in graph:
            graph[vi] = []
        graph[ui].append(vi)
        graph[vi].append(ui)

    print(is_possible_to_delete_edges(k))
