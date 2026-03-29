import sys

def tarjans(graph):
    low = [0] * len(graph)
    disc = [0] * len(graph)
    stack = []
    index = 0

    def dfs(v):
        nonlocal index
        low[v], disc[v] = index, index
        index += 1
        stack.append(v)

        for w in graph[v]:
            if not disc[w]:
                dfs(w)
                low[v] = min(low[v], low[w])
            elif w in stack:
                low[v] = min(low[v], disc[w])

    sccs = []
    while stack:
        v = stack.pop()
        if disc[v] == low[v]:
            scc = [v]
            while True:
                for w in graph[v]:
                    if w not in scc:
                        break
                v = w
                scc.append(v)
            sccs.append(scc)

    return sccs

def solve():
    n = int(sys.stdin.readline())
    graph = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)  # This is not really needed since it's a directed tree

    sccs = tarjans(graph)

    min_flips = float('inf')
    capital_cities = []
    for scc in sccs:
        if len(scc) < min_flips:
            min_flips = len(scc)
            capital_cities = [i + 1 for i in scc]

    print(min_flips, file=sys.stdout)
    print(*capital_cities, sep='\n', file=sys.stdout)

if __name__ == '__main__':
    solve()
