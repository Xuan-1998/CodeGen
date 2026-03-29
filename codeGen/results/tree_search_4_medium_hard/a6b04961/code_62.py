import heapq
from collections import defaultdict

def max_hedgehog_beauty():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    pq = [(0, [])]
    dp = defaultdict(list)

    while pq:
        total_beauty, path = heapq.heappop(pq)
        if len(path) > 1 or not edges:
            break

        for end, edge in enumerate(edges):
            if edge[0] == path[-1]:
                edges.pop(end)
                new_path = path + [edge[1]]
                total_beauty += 1
                heapq.heappush(pq, (total_beauty, new_path))

    return total_beauty

print(max_hedgehog_beauty())
