import sys

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))

    connected_components = {}
    xor_sums = {}

    def dfs(node, parent_value):
        nonlocal connected_components, xor_sums
        value = values[node]
        xor_sum = 0
        for child in range(n):
            if (child not in edges[edges.index((parent_value, node)):]) and child != parent_value:
                child_xor_sum = dfs(child, value)
                xor_sum ^= child_xor_sum
                break
        connected_components.setdefault(xor_sum, []).append(value)
        return xor_sum

    for node in range(1, n):
        dfs(node, 0)

    max_xor_sum = max(xor_sums.values())

    # Check the conditions
    for component in connected_components.get(max_xor_sum, []):
        if values.index(component) == 0:
            continue
        xor_sum = 0
        for child in range(n):
            if (child not in edges[edges.index((component, node)):]) and child != values.index(component):
                xor_sum ^= dfs(child, component)
                break
        if xor_sum != max_xor_sum:
            return "NO"

    # Delete edges if possible
    deleted_edges = 0
    for edge in edges[:]:
        u, v = edge
        xor_sum = xor_sums.get(xor_sums[max_xor_sum].index(u), 0)
        for child in range(n):
            if (child not in edges[edges.index((u, v)):]) and child != v:
                xor_sum ^= dfs(child, u)
                break
        if xor_sum == max_xor_sum:
            deleted_edges += 1
            edges.remove(edge)

    return "YES" if deleted_edges <= k-1 else "NO"

print(solve())
