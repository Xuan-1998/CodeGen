def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))

    def dfs(node, parent):
        connected_component = [values[node]]
        for neighbor in edges:
            if neighbor[0] == node and neighbor[1] != parent:
                connected_component.extend(dfs(neighbor[1], node))
        return connected_component

    xor_values = set()
    for i in range(n):
        connected_component = dfs(i, -1)
        xor_value = 0
        for value in connected_component:
            xor_value ^= value
        if xor_value not in xor_values:
            print("NO")
            return
        xor_values.add(xor_value)

    print("YES")

solve()
