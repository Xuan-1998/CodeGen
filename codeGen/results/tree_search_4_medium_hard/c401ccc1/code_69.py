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

def infinite_zoo(q):
    disjoint_set = DisjointSet()
    for _ in range(q):
        u, v = map(int, input().split())
        and_uv = u & v
        if and_uv == v:
            if find_path(u, v, and_uv, disjoint_set):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")

def find_path(u, v, and_v, disjoint_set):
    visited = set()
    stack = [(u, u & v)]
    while stack:
        vertex, and_vertex = stack.pop()
        if vertex == v:
            return True
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in [x for x in range(2**30) if (vertex & x) == and_vertex]:
                stack.append((neighbor, vertex & neighbor))
    return False

if __name__ == "__main__":
    q = int(input())
    infinite_zoo(q)

