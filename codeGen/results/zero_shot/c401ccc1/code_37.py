class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = set()
        self.graph[u].add(v)

    def has_path(self, u, v):
        if u not in self.graph:
            return False

        visited = set()

        def dfs(w):
            if w == v:
                return True
            if w in visited:
                return False
            visited.add(w)
            for neighbor in self.graph[w]:
                if dfs(neighbor):
                    return True
            return False

        return dfs(u)

    def solve(self, q):
        for _ in range(q):
            u, v = map(int, input().split())
            if self.has_path(u, v):
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    graph = Graph()
    q = int(input())
    for _ in range(q):
        u, v = map(int, input().split())
        graph.add_edge(u, v)
    graph.solve(q)

