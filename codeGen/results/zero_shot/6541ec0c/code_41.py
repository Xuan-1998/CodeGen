def dfs(node, parent, xor_value):
    if node not in tree:
        return xor_value
    for neighbor in tree[node]:
        if neighbor == parent:
            continue
        new_xor_value = xor_value ^ values[neighbor]
        result = dfs(neighbor, node, new_xor_value)
        if result != xor_value:
            return "NO"
    return "YES"

for _ in range(n_test_cases):
    n, k = map(int, sys.stdin.readline().split())
    values = list(map(int, sys.stdin.readline().split()))
    edges = []
    for _ in range(n-1):
        ui, vi = map(int, sys.stdin.readline().split())
        edges.append((ui, vi))
    
    # Build the tree
    tree = {}
    for edge in edges:
        ui, vi = edge
        if ui not in tree:
            tree[ui] = []
        if vi not in tree:
            tree[vi] = []
        tree[ui].append(vi)
        tree[vi].append(ui)

    # Determine whether it is possible to satisfy the condition
    for node in tree:
        xor_value = values[node]
        result = dfs(node, None, xor_value)
        if result == "NO":
            print("NO")
            break
    else:
        print("YES")
