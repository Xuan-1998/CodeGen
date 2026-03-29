from collections import defaultdict
from functools import lru_cache

def max_hedgehog_bauty(n, m, edges):
    @lru_cache(None)
    def dp(tail, used_edges):
        if len(tail) == n:
            return 0
        best = float('inf')
        for i in range(m):
            u, v = edges[i]
            if (u not in tail and v not in tail) or (u in tail and v not in tail) or (v in tail and u not in tail):
                used_edges.add(i)
                new_tail = tail + [u] if u in tail else tail + [v]
                best = min(best, dp(new_tail, used_edges) + 1)
                used_edges.remove(i)
        return best

    edges.sort(key=lambda x: (x[0], x[1]))
    used_edges = set()
    max_beauty = float('inf')
    for i in range(m):
        u, v = edges[i]
        if (u == edges[i-1][1] and len(used_edges) > 0) or (v == edges[i-1][1] and len(used_edges) > 0):
            used_edges.add(i)
            new_tail = [u] if i == 0 else edges[i-1][1:]
            max_beauty = min(max_beauty, dp(new_tail, used_edges) + 1)
    return max_beauty

if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [(int(x), int(y)) for x in range(m) for y in input().split()]
    print(max_hedgehog_bauty(n, m, edges))
