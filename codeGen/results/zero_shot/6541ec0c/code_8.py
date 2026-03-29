import sys
from collections import defaultdict

def solve():
    n, k = map(int, sys.stdin.readline().split())
    values = list(map(int, sys.stdin.readline().split()))
    tree_edges = []
    
    for _ in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        tree_edges.append((u, v))
        
    xor_values = defaultdict(set)
    
    for i in range(len(tree_edges)):
        parent = tree_edges[i][0]
        child = tree_edges[i][1]
        
        while child != 0:
            xor_values[parent].add(values[child-1])
            child = values[child-1]
            
    connected_components = set()
    
    for node, value_set in xor_values.items():
        if len(value_set) == 1:
            connected_components.add(tuple(sorted(list(value_set))))
        else:
            connected_components.add(0)
            
    return "YES" if len(connected_components) <= k else "NO"

print(solve())
