import sys

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))

    # Initialize XOR of each connected component
    xor_components = [0] * n

    def dfs(node, parent):
        # Calculate bitwise XOR of values in this subtree
        xor_subtree = 0
        for neighbor in edges:
            if neighbor[0] == node or neighbor[1] == node:
                xor_neighbor = dfs(neighbor[0] if neighbor[0] != node else neighbor[1], node)
                xor_subtree ^= xor_neighbor

        # Check if this XOR is consistent across all components
        for i in range(n):
            xor_components[i] -= xor_subtree ^ values[i]

    dfs(0, -1)  # Start DFS from node 0

    # Print the answer
    if any(xor_component != 0 for xor_component in xor_components):
        print("NO")
    else:
        print("YES")

if __name__ == "__main__":
    solve()
