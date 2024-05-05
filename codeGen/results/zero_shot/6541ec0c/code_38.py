import sys

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))

    # Find all connected components
    parent = list(range(n))
    rank = [0]*n
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x == root_y:
            return False
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
            if rank[root_x] == rank[root_y]:
                rank[root_y] += 1
        return True

    # Compute bitwise XOR for each component
    xor_values = {}
    for u, v in edges:
        union(u, v)
    for i in range(n):
        x = find(i)
        if x not in xor_values:
            xor_values[x] = values[i]
        else:
            xor_values[x] ^= values[i]

    # Check if all components have the same XOR value
    same_xor = list(set(xor_values.values()))
    if len(same_xor) == 1:
        return "YES"
    else:
        return "NO"

print(solve())
