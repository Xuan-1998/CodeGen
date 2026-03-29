import sys

def solve():
    n = int(sys.stdin.readline().strip())
    k = int(sys.stdin.readline().strip())
    values = list(map(int, sys.stdin.readline().split()))
    edges = []
    for _ in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
    tree = {i: [] for i in range(1, n+1)}
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    visited = set()
    def dfs(node):
        visited.add(node)
        for neighbor in tree[node]:
            if neighbor not in visited:
                dfs(neighbor)

    components = {}
    for node in range(1, n+1):
        if node not in visited:
            component = []
            dfs(node)
            for node in visited.copy():
                if node not in component:
                    component.append(node)
            components[len(component)] = component

    xors = []
    for _, component in sorted(components.items()):
        xor = 0
        for node in component:
            xor ^= values[node-1]
        xors.append(xor)

    if len(set(xors)) == 1:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
