class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.adj[u].append(v)

    def dfs(self, city, parent, depth):
        return max((depth + 1), *self.dfs(child, city, depth + 1) if child != parent else (depth,) for child in self.adj[city])

    def solve(self):
        capital = min(range(self.n), key=lambda i: len(self.adj[i]))
        reversed_edges = sum(max(self.dfs(i, -1, 0) for i in range(self.n)) for _ in range(self.n))
        return [reversed_edges], [str(capital)]

if __name__ == "__main__":
    n = int(input())
    graph = Graph(n)
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph.add_edge(u-1, v-1)
    print(*graph.solve(), sep='\n')
