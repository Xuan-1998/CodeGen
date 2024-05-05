import sys

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    graph = {}
    for _ in range(n - 1):
        u, v = map(int, input().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    # Your code here

if __name__ == "__main__":
    solve()
