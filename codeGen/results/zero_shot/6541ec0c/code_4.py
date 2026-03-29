import sys
from collections import defaultdict

def process_input():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))
    return n, k, values, edges

def dfs(node, parent, component):
    visited = set()
    stack = [node]
    while stack:
        curr_node = stack.pop(0)
        if curr_node not in visited:
            visited.add(curr_node)
            stack.extend([child for child in edges if child[0] == curr_node and child[1] != parent])
            component[curr_node] = next((value for value in values if value not in visited), None)

def process_tree(n, k, values, edges):
    components = defaultdict(dict)
    for node in range(1, n+1):
        dfs(node, -1, components[node])
    xor_values = []
    for node in range(1, n+1):
        xor_value = next((value for value in values if value not in components[node]), None)
        xor_values.append(xor_value)

    if len(set(xor_values)) == 1:
        print("YES")
    else:
        print("NO")

n, k, values, edges = process_input()
process_tree(n, k, values, edges)
