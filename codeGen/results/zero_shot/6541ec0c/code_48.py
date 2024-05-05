class DisjointSet:
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
        self.parent[root_x] = root_y

def can_delete_edges(n, k, edges, node_values):
    disjoint_set = DisjointSet()
    for i in range(1, n+1):
        disjoint_set.make_set(i)

    for u, v in edges:
        disjoint_set.union(u, v)
        xor_sum = 0
        for node in set([u, v]):
            xor_sum ^= node_values[node]
        if any(node_values[i] ^ xor_sum != 0 for i in disjoint_set.find(u)):
            return "NO"
    return "YES" if len(disjoint_set.parent) - 1 <= k else "NO"

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        node_values = list(map(int, input().split()))
        edges = []
        for _ in range(n-1):
            u, v = map(int, input().split())
            edges.append((u, v))
        print(can_delete_edges(n, k, edges, node_values))

if __name__ == "__main__":
    main()
