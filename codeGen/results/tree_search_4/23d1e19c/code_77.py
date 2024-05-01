import heapq

def min_max_recomputation(graph, path):
    n = len(graph)
    memo = {}
    pq = [(0, 0, [path[0]])]  # (min, max, path)

    while pq:
        min_recomp, max_recomp, p = heapq.heappop(pq)
        if p[-1] == graph[-1]:
            return min_recomp, max_recomp
        for v in range(n):
            if v not in p and (v, p) not in memo:
                new_p = list(p)
                new_p.append(v)
                if v == graph[0]:
                    new_min_recomp = 0
                    new_max_recomp = min(len(path) - 1, max_recomp + len(new_p) - len(p))
                else:
                    shortest_path = dijkstra(graph, p[-1], v)
                    new_min_recomp = max(min_recomp, len(shortest_path) - 1)
                    new_max_recomp = min(max_recomp + len(shortest_path) - len(p), len(path) - 2)
                memo[(v, p)] = (new_min_recomp, new_max_recomp)
                heapq.heappush(pq, (new_min_recomp, new_max_recomp, new_p))

    return -1, -1


def dijkstra(graph, s, t):
    n = len(graph)
    d = [float('inf')] * n
    d[s] = 0
    pq = [(0, s)]
    while pq:
        dist, v = heapq.heappop(pq)
        if v == t:
            return d[:t]
        for u in graph[v]:
            if d[u] > dist + 1:
                d[u] = dist + 1
                heapq.heappush(pq, (d[u], u))
    return [0]


def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
    k = int(input())
    path = list(map(int, input().split()))
    min_recomp, max_recomp = min_max_recomputation(graph, path)
    print(min_recomp, max_recomp)


if __name__ == "__main__":
    main()
