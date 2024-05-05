import sys

def tree_xor_edges():
    n, k = map(int, input().split())
    node_values = list(map(int, input().split()))
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))

    xor_values = set()
    for edge in edges:
        u, v = edge
        xor_values.add(node_values[u] ^ node_values[v])

    max_components = k  # at most k-1 edges can be deleted
    for component_xor in set(range(2**30)):  # all possible XOR values
        if component_xor not in xor_values:
            max_components -= 1

    return "YES" if max_components >= 0 else "NO"

if __name__ == "__main__":
    while True:
        try:
            print(tree_xor_edges())
        except ValueError:
            break
