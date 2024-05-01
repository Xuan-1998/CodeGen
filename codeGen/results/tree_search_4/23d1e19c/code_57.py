import sys
from collections import deque

def main():
    n, m = map(int, input().split())
    graph = {i: [] for i in range(1, n+1)}
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    k = int(input())
    path = list(map(int, input().split()))
    memo = {}

    def dp(v):
        if v == path[k-1]:
            return 0, 0

        if (v,) in memo:
            return memo[(v,)]

        min_rec, max_rec = float('inf'), 0
        for u in graph[v]:
            rec, _ = dp(u)
            new_min = min(min_rec, rec + 1)
            new_max = max(max_rec, rec + 1)
            min_rec, max_rec = new_min, new_max

        memo[(v,)] = (min_rec, max_rec)
        return min_rec, max_rec

    min_rec, max_rec = dp(path[0])
    print(min_rec+1, max_rec+1)

if __name__ == "__main__":
    main()
