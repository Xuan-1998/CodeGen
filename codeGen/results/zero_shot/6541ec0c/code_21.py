def solve_case(n, k, edges):
    total_xor = sum(xor_values)
    
    visited_nodes = set()
    component_xors = {}
    
    def dfs(node, parent_value=0):
        nonlocal total_xor
        xor_values[node-1] ^= parent_value
        visited_nodes.add(node)
        
        for neighbor in neighbors:
            if neighbor not in visited_nodes and xor_values[neighbor-1] != parent_value:
                component_xors[frozenset(visited_nodes)] = xor_values[node-1]
                total_xor = sum(xor_values)
                return
        
        for neighbor in neighbors:
            dfs(neighbor, xor_values[node-1])
    
    xor_values = [int(node_value) for node_value in values]
    edges.sort(key=lambda x: xor_values[x[0]-1] if x[0] < x[1] else xor_values[x[1]-1])
    
    root = 1
    for edge in edges:
        ui, vi = edge
        if xor_values[ui-1] != xor_values[vi-1]:
            component_xors[frozenset({root})] = xor_values[root-1]
            total_xor = sum(xor_values)
            break
        
    for component in component_xors:
        if any(xor_values[node-1] != component_xors[component] for node in component):
            return "NO"
    
    return "YES"

while True:
    n, k = map(int, input().split())
    if not (n and k):
        break
    
    xor_values = [int(node_value) for _ in range(n)]
    edges = []
    
    for _ in range(n-1):
        ui, vi = map(int, input().split())
        edges.append((ui, vi))
        
    print(solve_case(n, k, edges))
