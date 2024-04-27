from collections import defaultdict

# Step 1: Graph Representation
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def remove_edge(self, u, v):
        self.graph[u].remove(v)
        self.graph[v].remove(u)

    def add_back_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

# Step 2: Find Connected Components
    def dfs(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited)

    def count_components(self):
        visited = [False] * (self.V + 1)
        count = 0
        for i in range(1, self.V + 1):
            if not visited[i]:
                self.dfs(i, visited)
                count += 1
        return count

# Read input and initialize graph
n, m = map(int, input().split())
graph = Graph(n)
edges = []

for _ in range(m):
    x, y = map(int, input().split())
    graph.add_edge(x, y)
    edges.append((x, y))

# Step 3: Simulate Experiments
k = int(input())
for _ in range(k):
    l, r = map(int, input().split())
    l -= 1  # Convert to 0-based index
    u, v = edges[l]

    # Remove the edge and count components
    graph.remove_edge(u, v)
    print(graph.count_components(), end=' ')

    # Add the edge back to the graph
    graph.add_back_edge(u, v)
