from collections import defaultdict

def infinite_zoo_queries():
    q = int(input())
    graph = defaultdict(int)
    for _ in range(q):
        u, v = map(int, input().split())
        if (u & v) == v:
            graph[u] = 1
        if u & v == v:
            graph[v] = 1

    visited = [False] * 2**30
    for i in range(2**30):
        if graph[i]:
            for j in range(i + 1, 2**30):
                if (i & j) == j and not visited[j]:
                    visited[j] = True

    results = []
    for _ in range(q):
        u, v = map(int, input().split())
        if visited[v]:
            results.append("YES")
        else:
            results.append("NO")

    print("\n".join(results))

if __name__ == "__main__":
    infinite_zoo_queries()
