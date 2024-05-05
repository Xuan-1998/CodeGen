import sys
from collections import defaultdict

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    edges = {}
    for _ in range(n-1):
        u, v = map(int, input().split())
        if u not in edges:
            edges[u] = []
        if v not in edges:
            edges[v] = []
        edges[u].append(v)
        edges[v].append(u)

    memo = defaultdict(lambda: [[False for _ in range(k+1)] for _ in range(10**9 + 1)])

    def dfs(node, edge_count):
        if node in memo[node][edge_count]:
            return memo[node][edge_count][node]
        if edge_count <= k-1:
            memo[node][edge_count][node] = True
            return True
        for child in edges.get(node, []):
            for child_edge_count in range(edge_count+1):
                if dfs(child, child_edge_count):
                    memo[node][edge_count][node] = True
                    return True
        memo[node][edge_count][node] = False
        return False

    for node in values:
        if not dfs(node, 0):
            print("NO")
            return
    print("YES")

if __name__ == "__main__":
    solve()
