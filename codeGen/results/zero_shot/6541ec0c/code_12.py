import sys

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))

    # Initialize the bitwise XOR sum for each node
    xor_sums = [0] * (n+1)
    for i in range(1, n+1):
        xor_sums[i] = values[i-1]

    # Traverse the tree using DFS and update the bitwise XOR sums
    visited = [False] * (n+1)
    for edge in edges:
        u, v = edge
        if not visited[u]:
            dfs(u, xor_sums, visited)
        if not visited[v]:
            dfs(v, xor_sums, visited)

    # Check if the bitwise XOR sums are equal for each connected component
    for i in range(1, n+1):
        if xor_sums[i] != xor_sums[1]:
            return "NO"
    return "YES"

def dfs(node, xor_sums, visited):
    visited[node] = True
    for neighbor in edges:
        if neighbor[0] == node or neighbor[1] == node:
            next_node = 1 if neighbor[0] == node else 2
            xor_sums[node] ^= xor_sums[next_node]
            dfs(next_node, xor_sums, visited)

if __name__ == "__main__":
    while True:
        try:
            print(solve())
        except ValueError:
            break
