class UnionFind:
    def __init__(self):
        self.parent = {}

    def make_set(self, x):
        self.parent[x] = x

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y

def can_delete_edges(n, k, values, edges):
    uf = UnionFind()
    for i in range(n):
        uf.make_set(i)

    for u, v in edges:
        root_u = uf.find(u)
        root_v = uf.find(v)
        if root_u != root_v:
            uf.union(root_u, root_v)

    xor_values = {}
    for node in uf.parent:
        component_xors = set()
        while True:
            next_node = node
            component_xors.add(values[next_node])
            node = uf.find(node)
            if node == next_node:
                break
        component_xor = 0
        for value in component_xors:
            component_xor ^= value
        xor_values[component_xor] = component_xors

    return len(xor_values) <= k

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        values = list(map(int, input().split()))
        edges = []
        for _ in range(n-1):
            u, v = map(int, input().split())
            edges.append((u, v))
        print("YES" if can_delete_edges(n, k, values, edges) else "NO")

if __name__ == "__main__":
    main()
