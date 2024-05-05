from collections import defaultdict
from functools import lru_cache

def solve():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    @lru_cache(None)
    def dfs(tail_length, tail_vertices):
        if len(tail_vertices) == n:
            return 0
        max_beauty = 0
        for v in set(graph[tail_vertices[-1]]).difference(tail_vertices):
            new_tail_length = len(tail_vertices)
            new_tail_vertices = tuple(sorted(set(tail_vertices + [v])))
            if new_tail_length > tail_length:
                max_beauty = max(max_beauty, (new_tail_length - tail_length) * dfs(new_tail_length, new_tail_vertices))
        return max_beauty

    print(dfs(0, ()))

if __name__ == "__main__":
    solve()
