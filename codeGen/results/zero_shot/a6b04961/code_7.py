import sys

def find_max_beauty():
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    for u, v in [map(int, sys.stdin.readline().split()) for _ in range(m)]:
        graph[u].append(v)
        graph[v].append(u)

    max_beauty = 0
    visited = [False] * (n + 1)
    tail_len = 0
    spine_count = 0

    def dfs(v, parent):
        nonlocal tail_len, spine_count
        if visited[v]:
            return
        visited[v] = True
        for neighbor in graph[v]:
            if neighbor == parent:
                continue
            if not visited[neighbor]:
                dfs(neighbor, v)
            elif neighbor != u + 1 and neighbor != v - 1:  # spine
                spine_count += 1

    u = 1
    while u <= n:
        if not visited[u]:
            tail_len = 0
            spine_count = 0
            dfs(u, -1)
            max_beauty = max(max_beauty, tail_len * (spine_count + 1))
        u += 1

    print(max_beauty)

if __name__ == "__main__":
    find_max_beauty()
