import sys
from collections import defaultdict

def tarjan(graph):
    index = [0]
    stack = []
    lowlinks = {}
    indexes = {}

    def strongconnect(v):
        indexes[v] = index[0]
        lowlinks[v] = index[0]
        index[0] += 1
        stack.append(v)

        for w in graph[v]:
            if w not in indexes:
                strongconnect(w)
                lowlinks[v] = min(lowlinks[v], lowlinks[w])
            elif w in stack:
                lowlinks[v] = min(lowlinks[v], indexes[w])

        if lowlinks[v] == indexes[v]:
            while True:
                w = stack.pop()
                lowlinks[w] = n
                if v != w:
                    break

    n = len(graph)
    for v in range(n):
        if v not in indexes:
            strongconnect(v)

    return indexes, lowlinks

def solve():
    n, m = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)

    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    indexes, lowlinks = tarjan(graph)
    max_beauty = 0

    for i in range(len(indexes)):
        if lowlinks[i] == n:
            tail_length = indexes[i]
            spine_count = sum(1 for j in range(n) if lowlinks[j] < n and (j not in graph[i] or graph[i].index(j) != -1))
            max_beauty = max(max_beauty, tail_length * spine_count)

    print(max_beauty)

solve()
