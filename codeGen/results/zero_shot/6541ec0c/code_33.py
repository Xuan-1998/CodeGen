import sys
from collections import defaultdict

def dfs(node, parent, parent_bitxor, nodes_in_component, bitxors):
    nodes_in_component.add(node)
    current_bitxor = 0
    for neighbor in nodes:
        if neighbor != parent:
            if neighbor not in nodes_in_component:
                new_bitxor = dfs(neighbor, node, parent_bitxor ^ (1 << nodes[node].index), nodes_in_component, bitxors)[1]
                bitxors.append((node, new_bitxor))
            else:
                current_bitxor ^= 1 << nodes[neighbor].index
    return nodes_in_component.copy(), current_bitxor

def solve():
    n, k = map(int, sys.stdin.readline().split())
    nodes = [int(x) for x in sys.stdin.readline().split()]
    edges = []
    for _ in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
    
    bitxors = []
    nodes_in_component = set()
    current_bitxor = 0
    parent = None
    for edge in edges:
        node1, node2 = edge
        if node1 not in nodes_in_component or node2 not in nodes_in_component:
            nodes_in_component, current_bitxor = dfs(node1, parent, current_bitxor, nodes_in_component, bitxors)
        else:
            if current_bitxor != 0 and (current_bitxor & (1 << nodes[node1].index)) == 0 and (current_bitxor & (1 << nodes[node2].index)) == 0:
                return "NO"
    
    return "YES"

print(solve())
