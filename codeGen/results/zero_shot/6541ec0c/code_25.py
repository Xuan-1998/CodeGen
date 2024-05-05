import sys

def solve():
    n, k = map(int, sys.stdin.readline().split())
    values = list(map(int, sys.stdin.readline().split()))
    edges = []
    for _ in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))

    # Initialize XOR value for each connected component
    xor_values = [0] * (n+1)

    # Calculate initial XOR values for each node
    for i in range(1, n+1):
        xor_values[i] = values[i-1]
        for j in range(i-1):
            if edges[j][0] == i or edges[j][1] == i:
                xor_values[i] ^= xor_values[edges[j][0]] ^ xor_values[edges[j][1]]

    # Delete at most k-1 edges and update XOR values
    deleted_edges = 0
    for edge in edges:
        if deleted_edges >= k:
            break
        u, v = edge
        xor_values[u] ^= values[v]
        xor_values[v] ^= values[u]
        deleted_edges += 1

    # Check if XOR values remain the same after deleting edges
    result = "YES"
    for i in range(1, n+1):
        xor_value = 0
        for j in range(i-1):
            if edges[j][0] == i or edges[j][1] == i:
                xor_value ^= xor_values[edges[j][0]] ^ xor_values[edges[j][1]]
        if xor_value != xor_values[i]:
            result = "NO"
            break

    print(result)

if __name__ == "__main__":
    solve()
