import sys

def solve():
    n, k = map(int, input().split())
    node_values = list(map(int, input().split()))
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))

    # Construct the tree
    tree = {}
    for edge in edges:
        u, v = edge
        if u not in tree:
            tree[u] = []
        if v not in tree:
            tree[v] = []
        tree[u].append(v)
        tree[v].append(u)

    # Perform DFS/BFS to traverse the tree and calculate bitwise XOR
    xor_values = {}
    visited = set()
    for node in tree:
        if node not in visited:
            component_xor = 0
            stack = [node]
            while stack:
                current_node = stack.pop()
                visited.add(current_node)
                component_xor ^= node_values[current_node-1]
                for neighbor in tree[current_node]:
                    if neighbor not in visited:
                        stack.append(neighbor)
            xor_values[component_xor] = True

    # Check if it's possible to delete edges
    can_delete_edges = False
    for value, _ in xor_values.items():
        if k >= len(xor_values) and all(node_values[i-1]^value == 0 for i in range(1, n+1)):
            can_delete_edges = True
            break

    print("YES" if can_delete_edges else "NO")

if __name__ == "__main__":
    solve()
